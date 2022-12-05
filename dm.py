from ctypes.wintypes import PLARGE_INTEGER

#----------------------------------ENTREE-----------------------------------------------
print("Bienvenue au restaurant Arai de Trappes\n")

print("LES ENTREES :\n")
print("1- Salade de chef\t\t22€")
print("2- Salade nicoise\t\t30€")
print("3- Salade grecque\t\t9€")
print("4- Salade italienne\t\t11€")
print("5- Pas d'entrée\t\t\t0€\n")


liste_entree = ["Salade de chef",12,"Salade nicoise",10,"Salade grecque",9, "Salade italienne",11,"Pas d'entée",0]
entree = "0"


while entree == "0":
    entree = input("Choisir votre entrée: ")

    if entree == "1":
        print("Vous avez choisi la salade de chef.") 
        prix_entree = liste_entree[1]
        nom_entree = liste_entree[0]
    elif entree == "2":
        print("Vous avez choisi la salade nicoise.")
        prix_entree = liste_entree[3]
        nom_entree = liste_entree[2]
    elif entree == "3":
        print("Vous avez choisi la salade grecque.")
        prix_entree = liste_entree[5]
        nom_entree = liste_entree[4]
    elif entree == "4":
        print("Vous avez choisi la italienne.")
        prix_entree = liste_entree[7]
        nom_entree = liste_entree[6]
    elif entree == "5":
        print("Vous ne désirez pas d'entrée")
        prix_entree = liste_entree[9]
        nom_entree = liste_entree[8]
        
    else:
        print("'\033[91m' Une erreur est surveue lors de la saise de l'entrée merci de bien vouloir choisir un chiffre compris entre 1 et 4 compris: '\033[0m'")
        entree == "0"
        entree = input("Choisir votre entrée: ")
    
 



#---------------------------------PLATS-----------------------------------------------#

print("LES PLATS :\n")
print("1- Firture de poissons\t\t25€")
print("2- Bavette de veau\t\t19€")
print("3- Saumon à la plancha\t\t22€")
print("4- Boeuf bourguignons\t\t16€")
print("5- Pas de plats\t\t\t0€\n")


liste_plats = ["Friture de poissons",25,"Bavette de veau",19,"Saumon à la plancha",22, "Boeuf bourguignons",16,"Pas de plats",0]
plats = "0"


while plats == "0":
    plats = input("Choisir votre plats: ")

    if plats == "1":
        print("Vous avez choisi la Friture de poissons.")
        prix_plats = liste_plats[1]
        nom_plats = liste_plats[0]
    elif plats == "2":
        print("Vous avez choisi la Bavette de veau.")
        prix_plats = liste_plats[3]
        nom_plats = liste_plats[2]
    elif plats == "3":
        print("Vous avez choisi le Saumon aà la plancha.")
        prix_plats = liste_plats[5]
        nom_plats = liste_plats[4]
    elif plats == "4":
        print("Vous avez choisi le Boeuf bourguignons.")
        prix_plats = liste_plats[7]
        nom_plats = liste_plats[6]

    elif plats == "5":
        print("Vous ne désirez pas de plats")
        prix_plats = liste_plats[9]
        nom_plats = liste_plats[8]
    else:
        print("'\033[91m' Une erreur est surveue lors de la saise de l'entrée merci de bien vouloir choisir un chiffre compris entre 1 et 4 compris: '\033[0m'") 
        plats == "0"
        plats = input("Choisir votre plats: ")
        

#---------------------------------DESSERTS-----------------------------------------------


print("LES ENTREES :\n")
print("1- Crème brulée\t\t7€")
print("2- Tiramisu\t\t8€")
print("3- Glace aux choix\t9€")
print("4- Panacota\t\t6€")
print("5- Pas de dessert\t0€\n")

liste_desserts = ["Crème brulée",7,"Tiramisu",8,"Glace aux choix",9, "Panacota",6,"Pas de desserts",0]
desserts = "0"


while desserts == "0":
    desserts = input("Choisir votre plats: ")

    if desserts == "1":
        print("Vous avez choisi la Crème brulée.\n")
        prix_desserts = liste_desserts[1]
        nom_desserts = liste_desserts[0]
    elif desserts == "2":
        print("Vous avez choisi le Tiramisu.\n")
        prix_desserts = liste_desserts[3]
        nom_desserts = liste_desserts[2]
    elif desserts == "3":
        print("Vous avez choisi une glace aux choix.\n")
        prix_desserts = liste_desserts[5]
        nom_desserts = liste_desserts[4]
    elif desserts == "4":
        print("Vous avez choisi la panacota.\n")
        prix_desserts = liste_desserts[7]
        nom_desserts = liste_desserts[6]
    elif plats == "5":
        print("Vous ne désirez pas de plats")
        prix_desserts = liste_desserts[9]
        nom_desserts = liste_desserts[8]
    else:
        print("'\033[91m' Une erreur est surveue lors de la saise de l'entrée merci de bien vouloir choisir un chiffre compris entre 1 et 4 compris: '\033[0m'")
        desserts == "0"
        desserts = input("Choisir votre desserts: ")

#---------------------------------CHOIX MENU-----------------------------------------------

print(f"Votre menue est le suivant :\033[93m\n\n{nom_entree}\n{nom_plats}\n{nom_desserts}\033[0m\n\n")

#---------------------------------CALCUL PRIX-----------------------------------------------abdelrahim



prix = 0

somme=prix_desserts+prix_plats+prix_entree
print(f"\033[92m__TOTAL A PAYER__ :\033[0m {prix_entree} + {prix_plats} + {prix_desserts} = \033[92m{somme}€ \033[0m")