#!/usr/bin/env python3
# coding: utf-8




import pygame, time
from pygame.locals import *
import random
import logging
import sys, os, multiprocessing



def init_game():
	"""Initialisation de la partie applicative"""
		
	logging.basicConfig(level=logging.DEBUG)

	logging.info("Chargement de la configuration...")
	
	
	
def init_graph():
	"""Initialisation de la partie graphique"""
	
	pygame.init() # Initialisation de pygame
	
	logging.info("Initialisation de pygame...")
	Screen = pygame.display.set_mode( (800, 600) )
	
	pygame.key.set_repeat(100, 20)
	
	logging.debug("Chargement des ressources...")
	
	
	return(Screen)
	


if __name__ == "__main__":
	"""Tâche principale"""
		
	init_game()

	fenetre = init_graph()
	
	logging.error("Lancement du jeu...")
	
	fond = pygame.image.load("background.jpg").convert()
	gumpa = pygame.image.load("perso.png").convert_alpha()
	gumpa2 = pygame.image.load("perso.png").convert_alpha()

	debut = time.time()
	compteur = 0
	continuer = 1
	#Boucle infinie
	while continuer:
		if time.time() > debut+1:
			logging.info(compteur)
			compteur = 0
			debut = time.time()
		
		fenetre.blit(fond, (100,100))
		fenetre.blit(gumpa, (300,300))
		fenetre.blit(gumpa2, (400,200))
	
		pygame.display.flip()
		compteur += 1

		
		for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
			if event.type == QUIT:     #Si un de ces événements est de type QUIT
				continuer = 0      #On arrête la boucle




	
	
