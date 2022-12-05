from random import *

aleatoire1 = randint(1, 100)
aleatoire2 = randint(1, 100)


print (f"Les nombres tiré aleatoirement sont {aleatoire1} et {aleatoire2}.")
somme = int(input("Entrez la somme des 2 nombres"))

if somme == aleatoire1 + aleatoire2  :print (f"Bravo !!!!")

else :print ("Dommage... Tu peux retenter ta chance !")