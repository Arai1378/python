# def calculer_ttc(ht,tva):
#     return ht*(1+tva)
# TTC = calculer_ttc(200,0.2)
# print(TTC,"euros")



# # HTT = 0

# saisie = 0

from cgitb import html


def saisir_valeur(texte):
    saisie = 0
    while saisie == 0:

        saisie_str = input(f"Saisir {texte} : ")

        try:
            saisie = int(saisie_str)
        except:
            print("Vous n'avez pas saise de valeur numérique.")
        else:
            if saisie == 0:
                print("Vous avez saise zéro")
                
            elif saisie < 0:
                print("Vous avez saise une valeur négative.")
                saisie = 0

    return saisie
        
tva = saisir_valeur("TVA")

if tva > 30:
    print("Le montant de la TVA depasse les 30% ")
    print("Fin du programme !")
        
else:
    print(f"Le montant de la TVA = {tva}")

    ht = saisir_valeur("le montant HT: ")
    

#ht = saisir_valeur("HT")
calcul = ht * ( 1 + tva / 100)

print(f"somme est egale a {calcul}")


# def saisirvaleur(texte):

#     saisie = 0
#     while saisie == 0:
#         saisie_str = input("Saisir {}".format(texte))
#         try:
#             saisie = int(saisie_str)
#         except:
#             print("Vous n'avez pas choisi de valeur numérique.")
#         else:
#             if saisie ==0:
#                 print("Vous avez saisi zéro")
#             elif saisie < 0:
#                 print("Vous avez choisi une valeur négative !")
#     return saisie

# tva = saisirvaleur("le montant de la TVA: ")
# if tva > 30:
#     print("Le montant de la TVA depasse les 30%")
#     print("Fin du programme !")
# else:
#     print(f"Le montant de la TVA = {tva}")

#     ht = saisirvaleur("le montant HT: ")
    