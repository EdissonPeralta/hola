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
// $Id: gMCDetectorConstruction.cc 101036 2016-11-04 09:00:23Z gcosmo $
//
/// \file gMCDetectorConstruction.cc
/// \brief Implementation of the gMCDetectorConstruction class

#include "gMCDetectorConstruction.hh"
#include "gMCEmCalorimeterSD.hh"

#include "G4FieldManager.hh"
#include "G4TransportationManager.hh"
#include "G4Mag_UsualEqRhs.hh"
#include "G4AutoDelete.hh"

#include "G4Material.hh"
#include "G4Element.hh"
#include "G4MaterialTable.hh"
#include "G4NistManager.hh"

#include "G4VSolid.hh"
#include "G4SubtractionSolid.hh"
#include "G4Box.hh"
#include "G4Tubs.hh"
#include "G4LogicalVolume.hh"
#include "G4VPhysicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4PVParameterised.hh"
#include "G4PVReplica.hh"
#include "G4UserLimits.hh"

#include "G4SDManager.hh"
#include "G4VSensitiveDetector.hh"
#include "G4RunManager.hh"
#include "G4GenericMessenger.hh"

#include "G4VisAttributes.hh"
#include "G4Colour.hh"

#include "G4ios.hh"
#include "G4SystemOfUnits.hh"

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

gMCDetectorConstruction::gMCDetectorConstruction()
: G4VUserDetectorConstruction(), 
  fGeLogical(nullptr), fVisAttributes()  

{
  ;
  // define commands for this class
  //  DefineCommands();
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

gMCDetectorConstruction::~gMCDetectorConstruction()
{
  // delete fMessenger;
  
  for (auto visAttributes: fVisAttributes) {
    delete visAttributes;
  }  
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

G4VPhysicalVolume* gMCDetectorConstruction::Construct()
{
  
  ConstructMaterials();
  // geometries --------------------------------------------------------------
  // experimental hall (world volume)
  G4bool checkOverlaps = true;

  auto worldSolid
    = new G4Box("worldBox",100.*cm,100.*cm,200.0*cm);
  auto worldLogical
    = new G4LogicalVolume(worldSolid,air,"worldLogical");
  auto worldPhysical
    = new G4PVPlacement(0,G4ThreeVector(),
			worldLogical,
			"worldPhysical",
			0,false,0);

  G4ThreeVector T0;    // identity translation 
  G4RotationMatrix R0; // identity rotation
  G4Transform3D T3D0; // identity transformation 
  T3D0 = G4Transform3D(R0,T0);    

  // for all the tubes:
  G4double MinPhi = 0*deg;  G4double MaxPhi = 360*deg; G4double tubeMinRad =0.0*cm;
  
  // Germanium
  G4double GeMaxRad = 3.11*cm;
  G4double GeHalfLength = 2.965*cm;
  
  // Ge-recipiente (container) construido por sustracción de dos sólidos
  
  G4double GeAl_paraDistance = .489*cm;
  G4double GeContThick = 0.15*cm;
  G4double GeContHalfThick = GeContThick/2; 
  G4double GeContMaxRad2 = 3.81*cm;
  G4double GeContMaxRad1 = GeContMaxRad2 - GeContThick;
  G4double GeContHalfLength1 = GeHalfLength + GeAl_paraDistance;
  G4double GeContHalfLength2 = GeContHalfLength1 + GeContHalfThick;
  /*
  auto motherSolid
    = new G4Tubs("motherSolid",tubeMinRad, GeContMaxRad2,GeContHalfLength2,MinPhi,MaxPhi);

  auto motherLogical
   = new G4LogicalVolume(motherSolid,air,"motherLogical");
  */
  auto tubeSolid1
    = new G4Tubs("tube1",tubeMinRad,GeContMaxRad1,GeContHalfLength1,MinPhi,MaxPhi);
 auto tubeSolid2
    = new G4Tubs("tube2",tubeMinRad,GeContMaxRad2,GeContHalfLength2,MinPhi,MaxPhi);
 
  G4SubtractionSolid* GeContainer
    = new G4SubtractionSolid("GeContainer",
			     tubeSolid2,
			     tubeSolid1,
			     0,
			     G4ThreeVector(0.0,0.0,0.0));

  GeContainerLogical = new G4LogicalVolume(GeContainer,aluminum,"GeContainerLogical");
    
  auto GeSolid
    = new G4Tubs("Ge",tubeMinRad,GeMaxRad,GeHalfLength,MinPhi,MaxPhi);

  fGeLogical = new G4LogicalVolume(GeSolid,sodiumIodide,"GeLogical");//llenado del detector
  G4ThreeVector TGe;    
  G4Transform3D T3DGe;
  
  TGe.setX(0.0*cm);  TGe.setY(0.0*cm); TGe.setZ(6.0*cm);
  R0= G4RotationMatrix();
  //R0.rotateX(0*deg);
   R0.rotateY(-45*deg);
  //R0.rotateZ(0*deg);
  T3DGe = G4Transform3D(R0,TGe);
    
  new G4PVPlacement(T3DGe,
  		    fGeLogical,
  		    "GePhysical",
  		    worldLogical,
  		    false,0,checkOverlaps);
  
  new G4PVPlacement(T3DGe,
  		    GeContainerLogical,
  		    "GeContainerPhysical",
  		    worldLogical,
  		    false,0,checkOverlaps);
  
  //  G4double z_Ge = -GeContHalfLength + GeHalfLength + 2*GeContHalfThick + GeAl_paraDistance;
  G4ThreeVector Tmother;
  G4Transform3D T3Dmother;
  Tmother.setX(0.0*cm); Tmother.setY(0.0*cm);
  G4double z_shift = 0.0*cm;
  G4double z_mother = GeHalfLength + 2*GeContHalfThick + GeAl_paraDistance + z_shift;
  Tmother.setZ(z_mother);
  R0= G4RotationMatrix();
  R0.rotateY(0*deg);
  R0.rotateX(0*deg);
  R0.rotateZ(0*deg);
  T3Dmother = G4Transform3D(R0,Tmother);    
  /*
  new G4PVPlacement(T3Dmother,
		    motherLogical,
		    "motherDet",
		    worldLogical,
		    false,0,checkOverlaps);
  */
  //········································
  //·········Creation of the Mortero 1·············
  //········································

  
  
  //Elements
  G4double a;
  G4double z;
  G4double density;
  G4double fractionMass;
  G4String name;
  G4String symbol;
  G4int nElem;
  
a = 40.078*g/mole;
  G4Element* elCa = new G4Element(name="Calcium", symbol="Ca", z=19., a);
 
a = 55.845*g/mole;
  G4Element* elFe = new G4Element(name="Iron", symbol="Fe", z=26., a);

a = 39.0983*g/mole;
  G4Element* elK = new G4Element(name="Potassium", symbol="K", z=19., a);

a = 24.305*g/mole;
  G4Element* elMg = new G4Element(name="Magnesium", symbol="Mg", z=11., a);

a = 32.065*g/mole;
  G4Element* elS = new G4Element(name="Sulfur", symbol="S", z=16., a);

a = 28.0855*g/mole;
  G4Element* elSi = new G4Element(name="Silicium", symbol="Si", z=14., a);

a = 15.9994*g/mole;
G4Element* elO = new G4Element(name="oxigen", symbol="O", z=8., a);

a = 1.00794*g/mole;
G4Element* elH = new G4Element(name="hydronige", symbol="H", z=1., a);

a = 26.98153*g/mole;
G4Element* elAl = new G4Element(name="Aluminum", symbol="Al", z=13., a);

a = 22.989776*g/mole;
G4Element* elNa = new G4Element(name="Sodium", symbol="Na", z=11., a);

  
//---------------------------------------------------------------------//

  
// sand
  SiO2 = new G4Material("SiO2",density= 2.200*g/cm3, nElem=2);
  SiO2->AddElement(elSi, 1);
  SiO2->AddElement(elO , 2);

// water
  water = new G4Material(name="water", density= 1.000*g/cm3, nElem=2);
  water->AddElement(elH, 2);
  water->AddElement(elO, 1);

// CaO :: Calcium oxide 
  CaO = new G4Material(name="CaO", density= 3.340*g/cm3, nElem=2);
  CaO->AddElement(elCa, 1);
  CaO->AddElement(elO, 1);

// Fe2O3 :: Iron(III) oxide 
  Fe2O3 = new G4Material(name="Fe2O3", density= 5.240*g/cm3, nElem=2);
  Fe2O3->AddElement(elFe, 2);
  Fe2O3->AddElement(elO, 3);

// Al2O3 :: Aluminium oxide 
  Al2O3 = new G4Material(name="Al2O3", density= 3.950*g/cm3, nElem=2);
  Al2O3->AddElement(elAl, 2);
  Al2O3->AddElement(elO, 3);

// MgO :: Magnesium oxide 
  MgO = new G4Material(name="MgO", density= 3.580*g/cm3, nElem=2);
  MgO->AddElement(elMg, 1);
  MgO->AddElement(elO, 1);

// SO3 :: Sulfur trioxide
  SO3 = new G4Material(name="SO3", density= 1.920*g/cm3, nElem=2);
  SO3->AddElement(elS, 1);
  SO3->AddElement(elO, 3);

// K2O :: Potassium oxide
  K2O = new G4Material(name="K2O", density= 2.350*g/cm3, nElem=2);
  K2O->AddElement(elK, 2);
  K2O->AddElement(elO, 1);

// Na2O :: Sodium oxide
  Na2O = new G4Material(name="Na2O", density= 2.270*g/cm3, nElem=2);
  Na2O->AddElement(elNa, 2);
  Na2O->AddElement(elO, 1);
  
  //·····································································
  
  //Mixture of the elements
  Morteros1 = new G4Material("Morteros1", density= 1.6025*g/cm3, nElem=9);

  Morteros1->AddMaterial(SiO2, fractionMass=0.0*perCent);
  Morteros1->AddMaterial(water, fractionMass=25.0*perCent);
  Morteros1->AddMaterial(CaO, fractionMass=44.5945*perCent);
  Morteros1->AddMaterial(Fe2O3, fractionMass=10.1351*perCent); 
  Morteros1->AddMaterial(Al2O3, fractionMass=6.081*perCent);
  Morteros1->AddMaterial(MgO, fractionMass=6.081*perCent); 
  Morteros1->AddMaterial(SO3, fractionMass=6.081*perCent);
  Morteros1->AddMaterial(K2O, fractionMass=1.4188*perCent); 
  Morteros1->AddMaterial(Na2O, fractionMass=0.60814*perCent);;
  
  // Placa
  G4double placa_hx = 4.8018*cm; // 9,6037
  G4double placa_hy = 4.8406*cm; // 9,6813
  G4double placa_hz = 6.5*cm; // the variation is 0.5 
  
  auto placaSolid
    = new G4Box("placa", placa_hx, placa_hy, placa_hz);
  
  
  
  fPlacaLogical = new G4LogicalVolume(placaSolid, Morteros1,"placaLogical");

  G4ThreeVector Tplaca;    
  G4Transform3D T3Dplaca;
  Tplaca.setX(4.5*cm);  Tplaca.setY(0.0*cm);
  G4double zPlaca = - placa_hz  ;
  Tplaca.setZ(zPlaca);
  T3Dplaca = G4Transform3D(R0,Tplaca);    
  new G4PVPlacement(T3Dplaca,
  		    fPlacaLogical,
  		    "placaPhysical",
  		    worldLogical,
  		    false,0,checkOverlaps);
  
    // visualization attributes ------------------------------------------------

  auto visAttributes = new G4VisAttributes(G4Colour(0.,0.,0.));
  visAttributes->SetVisibility(false);
  worldLogical->SetVisAttributes(visAttributes);
  fVisAttributes.push_back(visAttributes);
  
  visAttributes = new G4VisAttributes(G4Colour(0.7,0.,0.));
  visAttributes->SetVisibility(true);
  visAttributes->SetForceSolid(true);
  fGeLogical->SetVisAttributes(visAttributes);
  fVisAttributes.push_back(visAttributes);
  
  visAttributes = new G4VisAttributes(G4Colour(0.6,0.6,0.2));
  visAttributes->SetVisibility(true);
  visAttributes->SetForceSolid(true);
  fPlacaLogical->SetVisAttributes(visAttributes);
  fVisAttributes.push_back(visAttributes);

  visAttributes = new G4VisAttributes(G4Colour(0.7,0.7,0.7));
  visAttributes->SetVisibility(true);
  visAttributes->SetForceSolid(false);
  GeContainerLogical->SetVisAttributes(visAttributes);
  fVisAttributes.push_back(visAttributes);
  
  
  
  // return the world physical volume ----------------------------------------
  
     G4cout << G4endl << "The geometrical tree defined are : " << G4endl << G4endl;
     DumpGeometricalTree(worldPhysical);
  
     return worldPhysical;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void gMCDetectorConstruction::ConstructSDandField()
{ 
  // turn sensitive Ge + NaI
  G4VSensitiveDetector* Ge;  
  //  G4VSensitiveDetector* NaI;  

  G4SDManager* sdManager = G4SDManager::GetSDMpointer();
  G4String SDname;
  
  Ge = new gMCEmCalorimeterSD(SDname="/Ge");
  sdManager->AddNewDetector(Ge);
  fGeLogical->SetSensitiveDetector(Ge);
  
}   

void gMCDetectorConstruction::ConstructMaterials()
{
  G4double a;
  G4double z;
  G4double density;
  G4double weightRatio, fractionMass;
  G4String name;
  G4String symbol;
  G4int nElem;

  // elements for mixtures and compounds
  a = 1.01*g/mole;
  G4Element* elH = new G4Element(name="Hydrogen", symbol="H", z=1., a);
  a = 12.01*g/mole;
  G4Element* elC = new G4Element(name="Carbon", symbol="C", z=6., a);
  a = 14.01*g/mole;
  G4Element* elN = new G4Element(name="Nitrogen", symbol="N", z=7., a);
  a = 16.00*g/mole;
  G4Element* elO = new G4Element(name="Oxigen", symbol="O", z=8., a);
  a = 23.0*g/mole;
  G4Element* elNa  = new G4Element("Sodium",symbol="Na" , z= 11., a);
  a = 26.98*g/mole;
  G4Element* elAl = new G4Element(name="Aluminum", symbol="Al", z=13., a);
  a = 126.9*g/mole;
  G4Element* elI = new G4Element(name="Iodine", symbol="I", z=53., a);
  a = 72.6*g/mole;
  G4Element* elGe = new G4Element(name="Germanium", symbol="Ge", z=32., a);
  a = 28.1*g/mole;
  G4Element* elSi = new G4Element(name="Silicon", symbol="Si", z=14., a);
  a = 63.546*g/mole;
  G4Element* elCu = new G4Element(name="Copper", symbol="Cu", z=29., a);
  a = 118.71*g/mole;
  G4Element* elTi = new G4Element(name="Tin", symbol="Ti", z=50., a);

  //germanium
  germanium = new G4Material("germanium", density= 5.32*g/cm3, nElem=1);
  germanium->AddElement(elGe,1);

  //aluminum
  aluminum = new G4Material("aluminum", density= 2.7*g/cm3, nElem=1);
  aluminum->AddElement(elAl,1);

  //copper
  copper = new G4Material("copper", density= 8.96*g/cm3, nElem=1);
  copper->AddElement(elCu,1);

  //tin
  tin = new G4Material("tin", density= 7.27*g/cm3, nElem=1);
  tin->AddElement(elTi,1);

  //NaI
  sodiumIodide = new G4Material("sodiumIodide", density= 3.67*g/cm3, nElem=2);
  sodiumIodide->AddElement(elNa,1);
  sodiumIodide->AddElement(elI,1);

  // carbon boards: Carbon at lower density
  carbonBoard = new G4Material("CarbonBoard", density= 2*g/cm3, nElem=1);
  carbonBoard->AddElement(elC,1);
  
  // arena1
  density = 1.500*g/cm3;
  arena1 = new G4Material(name="arena1", density, nElem=2);
  arena1->AddElement(elSi, 1);
  arena1->AddElement(elO, 2);

  // water
  density = 1.000*g/cm3;
  water = new G4Material(name="water", density, nElem=2);
  water->AddElement(elH, 2);
  water->AddElement(elO, 1);

  // sand
  SiO2 = new G4Material("SiO2",density= 2.200*g/cm3, nElem=2);
  SiO2->AddElement(elSi, 1);
  SiO2->AddElement(elO , 2);

  // humid sand
  humidSand = new G4Material("humidSand", density= 1.23*g/cm3, nElem=2);
  humidSand->AddMaterial(SiO2, fractionMass=100.0*perCent);
  humidSand->AddMaterial(water, fractionMass=0.0*perCent);  

  // Air
  density = 1.29*mg/cm3;
  air = new G4Material(name="Air", density, nElem=2);
  air->AddElement(elN, weightRatio=.7);
  air->AddElement(elO, weightRatio=.3);

  // Lead
  a = 207.19*g/mole;
  density = 11.35*g/cm3;
  lead = new G4Material(name="Lead", z=82., a, density);

  // Acrylonitrile
  density = 0.81*g/cm3;
  acrylonitrile = new G4Material(name="acrylonitrile", density, nElem=3);
  acrylonitrile->AddElement(elC, 3);
  acrylonitrile->AddElement(elH, 3);
  acrylonitrile->AddElement(elN, 1);

  // Polipropileno
  density = 0.85*g/cm3;
  polipropileno = new G4Material(name="polipropileno", density, nElem=2);
  polipropileno->AddElement(elC, 3);
  polipropileno->AddElement(elH, 6);

  // acrylic (polymethyl methacrylate)
  density = 1.19*g/cm3;
  acrylic = new G4Material(name="acrylic", density, nElem=3);
  acrylic->AddElement(elC, 5);
  acrylic->AddElement(elO, 2);
  acrylic->AddElement(elH, 8);

  // Polystyrene
  // experimental value: 0.0122 g/cm^3
  density = 0.0122*g/cm3;
  polystyrene = new G4Material(name="polystyrene", density, nElem=2);
  polystyrene->AddElement(elC, 1);
  polystyrene->AddElement(elH, 1);

  // LN2 (liquid nitrogen )
  density = 0.807*g/cm3;
  LN2 = new G4Material(name="LN2", density, nElem=1);
  LN2->AddElement(elN, 1);
  
  G4cout << G4endl << "The materials defined are : " << G4endl << G4endl;
  G4cout << *(G4Material::GetMaterialTable()) << G4endl;
}

void gMCDetectorConstruction::DestroyMaterials()
{
  // Destroy all allocated elements and materials
  size_t i;
  G4MaterialTable* matTable = (G4MaterialTable*)G4Material::GetMaterialTable();
  for(i=0;i<matTable->size();i++)
  { delete (*(matTable))[i]; }
  matTable->clear();
  G4ElementTable* elemTable = (G4ElementTable*)G4Element::GetElementTable();
  for(i=0;i<elemTable->size();i++)
  { delete (*(elemTable))[i]; }
  elemTable->clear();
}

void gMCDetectorConstruction::DumpGeometricalTree(G4VPhysicalVolume* aVolume,G4int depth)
{
  for(int isp=0;isp<depth;isp++)
  { G4cout << "  "; }
  G4cout << aVolume->GetName() << "[" << aVolume->GetCopyNo() << "] "
         << aVolume->GetLogicalVolume()->GetName() << " "
         << aVolume->GetLogicalVolume()->GetNoDaughters() << " "
         << aVolume->GetLogicalVolume()->GetMaterial()->GetName();
  if(aVolume->GetLogicalVolume()->GetSensitiveDetector())
  {
    G4cout << " " << aVolume->GetLogicalVolume()->GetSensitiveDetector()
                            ->GetFullPathName();
  }
  G4cout << G4endl;
  for(int i=0;i<aVolume->GetLogicalVolume()->GetNoDaughters();i++)
  { DumpGeometricalTree(aVolume->GetLogicalVolume()->GetDaughter(i),depth+1); }
}
