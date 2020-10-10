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
// $Id: gMCDetectorConstruction.hh 101036 2016-11-04 09:00:23Z gcosmo $
//
/// \file gMCDetectorConstruction.hh
/// \brief Definition of the gMCDetectorConstruction class

#ifndef gMCDetectorConstruction_h
#define gMCDetectorConstruction_h 1

#include "globals.hh"
#include "G4VUserDetectorConstruction.hh"
#include "G4RotationMatrix.hh"
#include "G4FieldManager.hh"

#include <vector>

class G4VPhysicalVolume;
class G4Material;
class G4VSensitiveDetector;
class G4VisAttributes;
class G4GenericMessenger;

/// Detector construction

class gMCDetectorConstruction : public G4VUserDetectorConstruction
{
public:
  gMCDetectorConstruction();
  virtual ~gMCDetectorConstruction();
  
  virtual G4VPhysicalVolume* Construct();
  virtual void ConstructSDandField();
  
private:  
  void ConstructMaterials();
  void DestroyMaterials();
  void DumpGeometricalTree(G4VPhysicalVolume* aVolume,G4int depth=0);
  
private:
  
  G4LogicalVolume* fGeLogical;
  G4LogicalVolume* fPlacaLogical;
  G4LogicalVolume* GeContainerLogical;
  
  std::vector<G4VisAttributes*> fVisAttributes;
  
private:
  G4Material* aluminum;
  G4Material* germanium;
  G4Material* copper;
  G4Material* tin;
  G4Material* lead;
  G4Material* sodiumIodide;
  G4Material* water;
  G4Material* air;
  G4Material* arena1;
  G4Material* humidSand;
  G4Material* SiO2;
  G4Material* acrylonitrile;
  G4Material* polipropileno;
  G4Material* polystyrene;
  G4Material* acrylic;
  G4Material* carbonBoard;
  G4Material* LN2;
  
};

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

#endif
