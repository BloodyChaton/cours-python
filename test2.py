#!/usr/bin/python
# coding: utf-8
x= raw_input ("Etes-vous heureux ? (o/n)")

if x =="o":
	print ("Veinard ! Partage ton bonheur")
#else :
#	y=raw_input("Cela te convient-il ? (o/n)")
#	if y=="o":
#	    print ("Aïe ! Prends un bonbon")
#	else:
#		print ("Parlons en alors")
elif raw_input ("Cela te convient-il (o/n)") == "o":
	print ("Aïe ! Prends un bonbon")
else:
	print ("Parlons-en alors")
	

print ("Fin du test")