# -*-coding:utf8-*
import os # On importe le module os

class Personnage:
	def __init__(self, nom, prenom, age):
		"""Seul le nom, le prénom et l'age sont définis lors de la création du personnage."""
		self.nom = nom
		self.prenom = prenom
		self.age = age
		
os.system("pause")
