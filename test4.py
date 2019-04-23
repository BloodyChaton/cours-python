#!/usr/bin/python
liste=[1,2,4]
x =len(liste)
if x > 3:
	y=x-1
	del liste[y]
elif x < 3:
    liste.append(3)
else:
	y=x+1
	liste.remove(y)
	liste.append(2)

print (liste)
