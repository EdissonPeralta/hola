//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************
//
// $Id: gMCEventAction.cc 101036 2016-11-04 09:00:23Z gcosmo $
//
/// \file gMCEventAction.cc
/// \brief Implementation of the gMCEventAction class

#include "gMCEventAction.hh"
#include "gMCEmCalorimeterHit.hh"
#include "gMCConstants.hh"
#include "gMCAnalysis.hh"

#include "G4Event.hh"
#include "G4RunManager.hh"
#include "G4EventManager.hh"
#include "G4HCofThisEvent.hh"
#include "G4VHitsCollection.hh"
#include "G4SDManager.hh"
#include "G4SystemOfUnits.hh"
#include "G4ios.hh"


//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

gMCEventAction::gMCEventAction()
: G4UserEventAction(), 
  fEmCalHC1ID(-1),
  fEmCalHC2ID(-1),
  fEmCalEdep(kNofEmCells, 0.)  
{
  // set printing per each event
  G4RunManager::GetRunManager()->SetPrintProgress(1);
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

gMCEventAction::~gMCEventAction()
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void gMCEventAction::BeginOfEventAction(const G4Event*)
{
  if (fEmCalHC1ID==-1) {
    auto sdManager = G4SDManager::GetSDMpointer();
    fEmCalHC1ID = sdManager->GetCollectionID("Ge/gammasColl");
    //    fEmCalHC2ID = sdManager->GetCollectionID("NaI/gammasColl");
  }
}     

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void gMCEventAction::EndOfEventAction(const G4Event* event)
{
  auto hce = event->GetHCofThisEvent();
  if (!hce) {
      G4ExceptionDescription msg;
      msg << "No hits collection of this event found." << G4endl; 
      G4Exception("gMCEventAction::EndOfEventAction()",
                  "gMCCode001", JustWarning, msg);
      return;
  }

  // Get hits collections 
  auto ecHC1 
    = static_cast<gMCEmCalorimeterHitsCollection*>(hce->GetHC(fEmCalHC1ID));
    
  auto ecHC2 
    = static_cast<gMCEmCalorimeterHitsCollection*>(hce->GetHC(fEmCalHC2ID));
        
  if ( (!ecHC1) || (!ecHC2) ) {
      G4ExceptionDescription msg;
      msg << "Some of hits collections of this event not found." << G4endl; 
      G4Exception("gMCEventAction::EndOfEventAction()",
                  "gMCCode001", JustWarning, msg);
      return;
  }   
  
  //
  // Fill histograms 
  // 
  
  // Get analysis manager
  auto analysisManager = G4AnalysisManager::Instance();
 
  // Fill histograms
 
  //  auto nhit  = ecHC1->entries();
  //  analysisManager->FillH1(0, nhit );

    // Ge energy 
  G4int totalEmHit1 = 0;
  G4double totalEmE1 = 0.;
  for (auto i=0;i<kNofEmCells;i++) {
    auto hit1 = (*ecHC1)[i];
    auto edep1 = hit1->GetEdep();
    if (edep1>0.) {
      totalEmHit1++;
      totalEmE1 += edep1;
    }
    fEmCalEdep[i] = edep1;
  }
  analysisManager->FillH1(0,totalEmE1/keV);
  
  //  nhit  = ecHC2->entries();
  // NaI energy 
  // G4int totalEmHit2 = 0;
  // G4double totalEmE2 = 0.;
  // for (auto i=0;i<kNofEmCells;i++) {
  //   auto hit2 = (*ecHC2)[i];
  //   auto edep2 = hit2->GetEdep();
  //   if (edep2>0.) {
  //     totalEmHit2++;
  //     totalEmE2 += edep2;
  //   }
  // }
  // analysisManager->FillH1(1,totalEmE2/keV);

  
  //
  // Print diagnostics
  // 
  
  auto printModulo = G4RunManager::GetRunManager()->GetPrintProgress();
  if ( printModulo==1000 || event->GetEventID() % printModulo == 0) return;
  
  auto primary = event->GetPrimaryVertex(0)->GetPrimary(0);
  G4cout 
    << G4endl
    << ">>> Event " << event->GetEventID() << " >>> Simulation truth : "
    << primary->GetG4code()->GetParticleName()
    << " " << primary->GetMomentum() << G4endl;
  
  // Ge detector
  G4cout << "Ge has " << totalEmHit1 << " hits. Total Edep is "
    << totalEmE1/keV << " (keV)" << G4endl;

}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
