#definition de la fonction
def indef(**args):   #**args permet de créer la fonctions avec un nombre indéfini d'arguments
    for i,j in args.items():
        print ("param =", i, ", valeur =", j)
indef(prénom= "Jean", nom = "Derieppe", age = 29)