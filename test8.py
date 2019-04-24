#!/usr/bin/python

def switch(l,a=0,b=-1):
	#a=l[0]
	#b=l[len(l)-1]
	c=l[a]
	l[a]=l[b]
	l[b]=c
	return l

liste=[1,4,6,9]
print liste
switch(liste)
print liste
