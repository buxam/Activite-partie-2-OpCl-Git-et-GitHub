# -*-coding:utf8-*
import os # On importe le module os

import random
from donnees import*

class Personnage:
	def __init__(self, nom, prenom, age):
		"""Seul le nom, le prénom et l'age sont définis lors de la création du personnage.
		Le lieu de résidence est par défaut "Paris" mais peut être modifié."""
		self.nom = nom
		self.prenom = prenom
		self.age = age
		self.residence = "Paris"
	def __repr__(self):
		"""Représentation de l'objet dans l'interpréteur."""
		return "{} {} a {} ans et réside à {}.\n".format(self.prenom, self.nom, self.age,self.residence)
	def __str__(self):
		"""Représentation de l'objet sous forme d'une chaîne de caractères."""
		return repr(self)
		
nom = input("Nom:")
prenom = input("Prénom:")
age = random.randrange(10,100)

ville = random.choice(liste_villes)

personnage = Personnage(nom,prenom,age)
personnage.residence = ville

print (personnage)
		
os.system("pause")
