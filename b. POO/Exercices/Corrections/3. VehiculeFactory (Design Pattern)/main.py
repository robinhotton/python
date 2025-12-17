from voiture import Voiture
from moto import Moto

# CREATION DES VÉHICULES
print(f"Création d'une voiture")
voiture: Voiture = Voiture.from_factory("Toyota", "Camry", 2022, 4)
print(f"Création d'une moto")
moto: Moto = Moto.from_factory("Harley-Davidson", "Sportster", 2023)


# METHODES DES VEHICULES
vehicules = [voiture, moto]
for vehicule in vehicules:
    class_name = vehicule.__class__.__name__
    print(f"\nNouveau véhicule")
    print(vehicule)
    print(f"la {class_name} roule à {vehicule.vitesse} km/h")
    print(f"la {class_name} accelere")
    vehicule.accelerer()
    print(f"la {class_name} roule à {vehicule.vitesse} km/h")
    print(f"la {class_name} s'est arreter")
    vehicule.arreter()
    print(f"la {class_name} roule à {vehicule.vitesse} km/h")
print(moto.acrobaties())


# SUPPRESSION DES OBJETS
# On vide le stockage avant la fin du programme
print("\nLibération de l'espace mémoire")
del voiture
del moto