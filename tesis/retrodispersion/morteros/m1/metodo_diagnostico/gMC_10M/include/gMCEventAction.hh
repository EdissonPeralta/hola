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
// $Id: gMCEventAction.hh 101036 2016-11-04 09:00:23Z gcosmo $
//
/// \file gMCEventAction.hh
/// \brief Definition of the gMCEventAction class

#ifndef gMCEventAction_h
#define gMCEventAction_h 1


#include "G4UserEventAction.hh"
#include "globals.hh"

#include <vector>

/// Event action

class gMCEventAction : public G4UserEventAction
{
public:
    gMCEventAction();
    virtual ~gMCEventAction();
    
    virtual void BeginOfEventAction(const G4Event*);
    virtual void EndOfEventAction(const G4Event*);

    std::vector<G4double>& GetEmCalEdep() { return fEmCalEdep; }
    
private:
    G4int fEmCalHC1ID;
    G4int fEmCalHC2ID;

    std::vector<G4double> fEmCalEdep;

};

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

#endif
