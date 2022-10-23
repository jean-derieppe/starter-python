def croissant(*args):
    myList = []
    for i in args:
        myList.append(i)
    myList.sort()
    print(myList)

croissant(4,6,8,13,14,19,35,74,99,150,168)
