#!/usr/bin/python
liste = [1,1]
print liste
def fibonacci(l):
	a=l[-1] + l[-2]
	l.append(a)
	return (l)

x = input("Taille de la liste ")
if len(liste) < x:
	for x in range (1,x-1):
		liste = fibonacci(liste)
		print liste
else:
	print liste
