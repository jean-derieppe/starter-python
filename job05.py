# définir les variables a et b par des entiers grâce à int(input(".."))
a = int(input("entrez la première valeur : "))
b = int(input("entrez la deuxième valeur : "))
#conditions si a est inférieur à b 
if a < b:
    for i in range(a+1,b): #boucle pour la rangé entre input a et b avec incrémentation affichant les nombres inclus dans l'interval
        print (i)
elif a > b:
    for i in range(a-1,b,-1): #boucle avec décrémentation affichant les nombres inclus dans l'interval
        print (i)
else:
         print ("Valeurs égales") # si les conditions a>b et a<b sont faulse , cela signifie que a == b alors print ("Valeurs égales")