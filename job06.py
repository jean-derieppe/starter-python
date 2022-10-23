#boucle qui n'affiche qu'un chevron jusqu'à ce qu'on indique "Au revoir"
test = input("> ")
while test != "Au revoir": # Boucle qui tourne tant que l'input(test) sera différente de Au revoir
    if test == "Bonjour": # si input est strictement égale a Bonjour, alors Bonjour à toi sera print et vu que test=input(">") est indéxé au même niveau que print cela permet à nouveau d'entrer une donnée
        print ("Bonjour à toi ")
        test = input("> ")
# While, quand test == Au revoir, on sort de la boucle while
exit()