#!/usr/bin/python
# coding: utf-8
'''
Ecrire un programme en python qui utiliser une fonction récursive qui implémente la recherche binaire sur une liste ordonnée
'''
def recherche_binaire(liste_initiale,a,b=0,c=-1):
	if b==c:
		return 0
	else:
		if c==-1:
			c=len(liste_initiale)
		moitie=(b+c)//2
		reference=liste_initiale[moitie]
		if reference == a :
			return moitie
		elif reference >a :
			b=0
			c=moitie-1
			return recherche_binaire(liste_initiale,a,b,c)
		else :
			b=moitie+1
			recherche_binaire (liste_initiale,a,b,c)
	

liste = [1,2,4,8,12,16,22,29,35,46,86,121,235,695]
resultat = recherche_binaire(liste,4)
print (resultat)


