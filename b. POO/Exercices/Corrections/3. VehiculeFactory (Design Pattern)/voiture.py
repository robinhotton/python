from vehicule import Vehicule

class Voiture(Vehicule):
    """Classe concrète Voiture. Classe fille de Véhicule.

    Attributs:
        marque (str): marque du véhicule.
        modele (str): modèle du véhicule.
        annee (int): année du véhicule.
        (Optional) nombre_portes (int): nombre de portes de la voiture. Par défaut à 3.
        vitesse (int): vitesse du véhicule. Fixer à 0.
        
    Méthodes:
        accelerer() -> None : permet d'accelerer le véhicule. 
        arreter() -> None : permet d'arrêter le véhicule.
    """
    def __init__(self, marque: str, modele: str, annee: int, nombre_portes: int = 3) -> None:
        super().__init__(marque, modele, annee)
        self.nombre_portes: int = nombre_portes
        
    def __str__(self):
        return f"Voiture[marque: {self.marque}, modele: {self.modele}, fabrication: {self.annee}, vitesse: {self.vitesse} km/h, nombre de portes: {self.nombre_portes}]"

    # GETTERS / SETTERS

    @property
    def nombre_portes(self) -> int:
        return self.__nombre_portes

    @nombre_portes.setter
    def nombre_portes(self, valeur) -> None:
        if valeur > 2:
            self.__nombre_portes = valeur
        else:
            raise ValueError("Le nombre de portes doit être supérieur à 2.")
        
    # METHODES

    def accelerer(self) -> None:
        self.vitesse += 10