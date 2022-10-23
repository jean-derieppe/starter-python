# âge=int(input("Bonjour, quel âge as-tu")) demande au lecteur d'entrer son âge qui sera un nbe entier, grâce à la commande int on peut définir un entier comme valeur de la variable (âge),
âge=int(input("Bonjour, quel âge as-tu ?\nEntre ton âge : "))
# if(âge>=18) :
#     print : signifie Si l'entier défini par la variable âge est supérieure ou égale à 18, imprimer ("chaîne de caractére")
if(âge>=18) :
    print("Tu es majeur \nBienvenue, tu peut accéder au site.")
# else :
#     print : signifie sinon (si l'entier est inférieur â 18 dans le cas de la variable âge)
else :
    print("Tu es mineur \nL'accés au site t'es refusé")