# -*-coding:utf8-*
import os # On importe le module os

import random

class Personnage:
	def __init__(self, nom, prenom, age):
		"""Seul le nom, le prénom et l'age sont définis lors de la création du personnage."""
		self.nom = nom
		self.prenom = prenom
		self.age = age
	def __repr__(self):
		"""Représentation de l'objet dans l'interpréteur."""
		return "{} {} a {} ans.".format(self.prenom, self.nom, self.age)
	def __str__(self):
		"""Représentation de l'objet sous forme d'une chaîne de caractères."""
		return repr(self)
		
nom = input("Nom:")
prenom = input("Prénom:")
age = random.randrange(10,100)

personnage = Personnage(nom,prenom,age)

print (personnage)
		
os.system("pause")
