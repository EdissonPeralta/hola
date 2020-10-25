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
// $Id: gMCPrimaryGeneratorAction.hh 101036 2016-11-04 09:00:23Z gcosmo $
//
/// \file gMCPrimaryGeneratorAction.hh
/// \brief Definition of the gMCPrimaryGeneratorAction class

#ifndef gMCPrimaryGeneratorAction_h
#define gMCPrimaryGeneratorAction_h 1

#include "G4VUserPrimaryGeneratorAction.hh"
#include "globals.hh"

//class G4ParticleGun;
class G4GeneralParticleSource;
class G4GenericMessenger;
class G4Event;
class G4ParticleDefinition;

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
 
class gMCPrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction
{
  public:
    gMCPrimaryGeneratorAction();    
   ~gMCPrimaryGeneratorAction();

  public:
    void GeneratePrimaries(G4Event*);

  private:
  //    G4ParticleGun* particleGun;
    G4GeneralParticleSource* particleGun;
  //    gMCDetectorConstruction* myDetector;
};

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

#endif
