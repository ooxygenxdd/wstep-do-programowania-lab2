with open("notwania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia)

with open("notwania_gieldowe.txt", "a") as plik:
    plik.write("\nALR, 113")

with open("notwania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia)
