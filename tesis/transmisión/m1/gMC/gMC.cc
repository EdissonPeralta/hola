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
// $Id: exampleB5.cc -> gMC 70284 2013-05-28 17:26:43Z perl $
//
/// \file examplegB5.cc -> gMC


#include "gMCDetectorConstruction.hh"
#include "gMCActionInitialization.hh"

#ifdef G4MULTITHREADED
#include "G4MTRunManager.hh"
#else
#include "G4RunManager.hh"
#endif

#include "G4UImanager.hh"
//#include "QGSP_BERT_HP.hh"
//#include "G4EmPenelopePhysics.hh"
//#include "G4StepLimiterPhysics.hh"
#include "G4PhysListFactory.hh"
#include "G4VModularPhysicsList.hh"

#include "G4VisExecutive.hh"
#include "G4UIExecutive.hh"

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

int main(int argc,char** argv)
{
// #ifdef G4UI_USE
//   // Detect interactive mode (if no arguments) and define UI session
//   //
   G4UIExecutive* ui = 0;
   if ( argc == 1 ) {
     ui = new G4UIExecutive(argc, argv);
   }
// #endif

  // Construct the default run manager
  //
#ifdef G4MULTITHREADED
  auto runManager = new G4MTRunManager;
#else
  auto runManager = new G4RunManager;
#endif

  //set random seed with system time
  G4long seed = time(NULL); // seed taken in some way from actual time 
  CLHEP::HepRandom::setTheSeed(seed);

  // Mandatory user initialization classes
  runManager->SetUserInitialization(new gMCDetectorConstruction);
  
  G4int verbose =1;
  G4PhysListFactory factory;
  G4VModularPhysicsList* physlist = factory.GetReferencePhysList("FTFP_BERT_PEN");
  physlist->SetVerboseLevel(verbose);
  runManager->SetUserInitialization(physlist);
  
  
  //FTFP_BERT* physicsList = new FTFP_BERT(verbose);
  //  auto physicsList = new QGSP_BERT_HP;
  //   auto physicsList = new G4EmPenelopePhysics();
  
  //  physicsList->RegisterPhysics(new G4StepLimiterPhysics());
  runManager->SetUserInitialization(physlist);

  //  G4cout << " despues runManager " << G4endl;
  
  // User action initialization
  runManager->SetUserInitialization(new gMCActionInitialization());

  // Visualization manager construction
  auto visManager = new G4VisExecutive;
  // G4VisExecutive can take a verbosity argument - see /vis/verbose guidance.
  // G4VisManager* visManager = new G4VisExecutive("Quiet");
  visManager->Initialize();
    
  // Get the pointer to the User Interface manager
  auto UImanager = G4UImanager::GetUIpointer();

  if ( argc != 1 ) {
    // execute an argument macro file if exists
    G4String command = "/control/execute ";
    G4String fileName = argv[1];
    UImanager->ApplyCommand(command+fileName);
  }
  else {
// #ifdef G4UI_USE
// #ifdef G4VIS_USE
     UImanager->ApplyCommand("/control/execute vis.mac"); 
// // #else
// //     UImanager->ApplyCommand("/control/execute init.mac"); 
// #endif
//      if (ui->IsGUI()) {
//     //      UImanager->ApplyCommand("/control/execute gui.mac");
//     }     
//     // start interactive session
     ui->SessionStart();
     delete ui;
// #endif
  }

  // Job termination
  // Free the store: user actions, physics_list and detector_description are
  // owned and deleted by the run manager, so they should not be deleted 
  // in the main() program !

  delete visManager;
  delete runManager;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
