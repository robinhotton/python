from abc import ABC, abstractmethod

class Vehicule(ABC):
    """Classe abstraite représentant un véhicule.

    Attributs:
        marque (str): marque du vehicule.
        modele (str): modèle du vehicule.
        annee (int): année du vehicule.
        vitesse (int): vitesse du véhicule.  Fixer à 0.
    
    Méthodes:
        accelerer() -> None : ABSTRAITE. Permettra d'accelerer le véhicule. 
        arreter() -> None : permet d'arrêter le véhicule.
        from_factory(*args) -> "Vehicule" : permet de créer une instance de la classe fille.
    """

    # CONSTRUCTEUR
    def __init__(self, marque: str, modele: str, annee: int):
        self.marque: str = marque
        self.modele: str = modele
        self.annee: int = annee
        self.vitesse: int = 0

    # AFFICHAGE
    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}[marque: {self.marque}, modele: {self.modele}, fabrication: {self.annee}, vitesse: {self.vitesse} km/h]"

    # DESTRUCTEUR
    def __del__(self) -> None: 
        class_name = self.__class__.__name__
        print(f"Objet {class_name} est détruit.")
        
    # GETTERS / SETTERS

    @property
    def marque(self) -> str:
        return self._marque

    @marque.setter
    def marque(self, valeur) -> None:
        self._marque = valeur

    @property
    def modele(self) -> str:
        return self._modele

    @modele.setter
    def modele(self, valeur) -> None:
        self._modele = valeur

    @property
    def annee(self) -> int:
        return self._annee

    @annee.setter
    def annee(self, valeur) -> None:
        self._annee = valeur

    @property
    def vitesse(self) -> int:
        return self._vitesse

    @vitesse.setter
    def vitesse(self, valeur) -> None:
        self._vitesse = valeur

    # METHODES

    @abstractmethod
    def accelerer(self) -> None:
        pass

    def arreter(self) -> None:
        self.vitesse = 0
    
    @classmethod
    def from_factory(cls, *args) -> "Vehicule":
        if cls == Vehicule:
            raise NotImplementedError("Utilisez une sous-classe de Vehicule.")
        return cls(*args)
