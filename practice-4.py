from time import perf_counter


personne = int(input("Age of first person"))
persontwo = int(input("Age of second person"))
personthree = int(input("Age of third person"))

if personne > persontwo and personne > personthree:
    print("Elder one is",personne)

elif persontwo > personne and persontwo > personthree:
    print("Elder one is",persontwo)

elif personthree > personne and personthree > persontwo:
    print("Elder one is",personthree)

if personne < persontwo and personne < personthree:
    print("Younger one is",personne)

elif persontwo < personne and persontwo < personthree:
    print("Younger one is",persontwo)

elif personthree < personne and personthree < persontwo:
    print("Younger one is",personthree)