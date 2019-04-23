#!/usr/bin/python
liste = []
x = input ("Taille de la liste ")
x =x+1
for x in range (1,x):
	y=x**2
	z=(x,y)
	liste.append(z)
	#autre possibilité : directement liste.append ((x,x**2))
print liste