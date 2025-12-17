from animal import Animal

class Chien(Animal):
    
    def __init__(self, nom: str, age: int) -> None:
        super().__init__(nom, age)
        
    def crier(self) -> str:
        return "Woof!"
    
    @classmethod
    def from_factory(cls, nom: str, age: int) -> "Chien":
        if len(nom) >= 3:
            return cls(nom, age)
        else:
            return None