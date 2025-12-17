from chien import Chien

chien = Chien("Skadi", 5)
print("nom:", chien.nom)
print("age:", chien.age)
print("crier:", chien.crier())
print("total:", Chien.nombre_animaux())

rex = Chien.from_factory("Rex", 3)
print("print:", rex) # Animal[nom:Rex, age:3 ans] car __str__ n'est pas redéfini dans Chien 
print("total:", Chien.nombre_animaux())

invalide = Chien.from_factory("R", 3)
print("print:", invalide)