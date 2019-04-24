#!/usr/bin/python
class Client:
	nombre_client=0
	def __init__(self,valeur1,valeur2):
		self.attribut1=valeur1
		self.attribut2=valeur2
		Client.nombre_client+=1
	def get_info(self):
		print ("Bonjour")
		print ("nom: ", self.attribut1, "compte: ",self.attribut2)
		print Client.nombre_client

Client1 = Client("MARTINON","007")
Client1.get_info()