palavra = "paralelepipedo"
cont = 0

for letra in palavra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        cont += 1
print("A palavra", palavra, "tem", cont, "vogais")