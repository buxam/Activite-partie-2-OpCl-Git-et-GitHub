# -*-coding:utf8-*
import os # On importe le module os

import random

class Personnage:
	def __init__(self, nom, prenom, age):
		"""Seul le nom, le prénom et l'age sont définis lors de la création du personnage."""
		self.nom = nom
		self.prenom = prenom
		self.age = age

		
nom = input("Nom:")
prenom = input("Prénom:")
age = random.randrange(0,100)

personnage = Personnage(nom,prenom,age)
		
os.system("pause")
