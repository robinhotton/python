from abc import ABC, abstractmethod # Abstract Base Class

class Animal(ABC):
    
    population: int = 0
    
    def __init__(self, nom: str, age: int) -> None:
        self.nom = nom
        self.age = age
        Animal.population += 1
        
    #######################
    # Getters and Setters #
    #######################
        
    @property
    def nom(self) -> str:
        return self._nom
    
    @nom.setter
    def nom(self, nom) -> None:
        self._nom = nom
        
    @property
    def age(self) -> str:
        return self._age
    
    @age.setter
    def age(self, age) -> None:
        self._age = age
        
    ###########
    # Methods #
    ###########

    @abstractmethod
    def crier(self) -> str:
        pass
    
    @staticmethod
    def nombre_animaux() -> int:
        return Animal.population
    
    #################
    # Magic Methods #
    #################
    
    def __str__(self) -> str:
        return f"Animal[nom:{self.nom}, age:{self.age} ans]"
    
    # def __str__(self) -> str:
    #     class_name = self.__class__.__name__.title()
    #     return f"{class_name}[nom:{self.nom}, age:{self.age} ans]"