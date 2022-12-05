note = int(input("Entree la note"))

if 18<= note<=20 :print (f"la note est de {note} est exellente")
elif 14<= note<18 :print (f"la note est de {note} est tres bien")
elif 10<= note<14 :print (f" la note est de {note} est assez bien")
elif 5<= note<10 :print (f" la note est de {note} est insuffisant")
elif 0<=note<5 :print (f" la note est de {note} est catastrophique")
else:
    print("Saisie incorrecte")