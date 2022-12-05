#------------------------------------------------------APPEL FICHIER ERREUR GESTION-----------------------------------------------------
from gestionErreurs import saisirvaleur
#------------------------------------------------------DEMANDER A L'UTILISATEUR DE------------------------------------------------------

print(" \nBonjour ce programme permet de calculer ton IMC.\n\n                          Pour commencer :\n")
poids = saisirvaleur(" votre poids en kg ")
taille = saisirvaleur(" votre taille en cm ")

#------------------------------------------------------CALCUL IMC ET CONVERSION---------------------------------------------------------

poids_float = float(poids)
taille_float = float(taille)
taille_metre = taille_float * 0.01

IMC_taille = taille_metre * taille_metre 
IMC = poids_float / IMC_taille

print(f"votre IMC est de {IMC}.\n")


#------------------------------------------------------CONDITION IMC--------------------------------------------------------------------

calcul = 0
while calcul == 0:
    if IMC <18.5 : 
        print("     Vous êtes en sous poids.")
        exit()
    elif -18.6< IMC  < 24.9:
        print("     Vous êtes normal.")
        exit()
    elif 25 < IMC < 29.9:
        print("     Vous êtes en surpoids.")
        exit()
    elif 30 < IMC < 34.9:
        print ("        Vous êtes en obésité.")
        exit()
    else:
        print ("        Vous êtes en obesité sévère.")
        exit()