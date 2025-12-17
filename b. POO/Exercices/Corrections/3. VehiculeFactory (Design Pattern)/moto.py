from vehicule import Vehicule

class Moto(Vehicule):
    """Classe concrète Voiture. Classe fille de Véhicule.

    Attributs:
        marque (str): marque du véhicule.
        modele (str): modèle du véhicule.
        annee (int): année du véhicule.
        vitesse (int): vitesse du véhicule.  Fixer à 0.
        
    Méthodes:
        accelerer() -> None : permet de accelerer le véhicule.
        arreter() -> None : permet d'arrêter le véhicule.
        acrobaties() -> str : permet de faire des 'wheel-in!'.
    """
    def __init__(self, marque: str, modele: str, annee: int):
        super().__init__(marque, modele, annee)

    # METHODES

    def accelerer(self) -> None:
        self.vitesse += 30

    def acrobaties(self) -> str:
        return "Wheel-in!"
