#------------------------------------------------------FICHIER ERREUR GESTION-----------------------------------------------------

def saisirvaleur(text):
    saisie = 0 
    while saisie == 0:
        str_saisie= input("Veuillez saisir{}:".format(text))
        try:
            saisie = int(str_saisie)

        except:
            print("Vous n'avez pas saisie de valeur numérique")
        else:
            if saisie <0:
                print("Vous avez choisi une valeur négative")
            elif saisie == 0:
                print("Vous avez saisi zéro")
            else :
                print("saisie correct\n")
                
    return saisie