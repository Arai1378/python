from gestionErreur import saisirvaleur

class IMC:
    def __init__(self,poids="poids",taille="taille"):
        self.poids = saisirvaleur("votre poids en Kg")
        self.taille = saisirvaleur("votre taille en cm")
       
    def afficher(self):
        print(f"Votre poids est : {self.poids} et votre taille est de : {self.taille}")

    def calculerIMC (self):
        self.taille /=100
        return self.poids/(self.taille**2)

    def afficherinfo(self):
        imc = self.calculerIMC()
        print("votre imc =",imc)

monIMC = IMC()
monIMC.afficherinfo()