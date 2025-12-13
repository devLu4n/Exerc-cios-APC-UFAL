frase = "Madonna rainha do pop"
count= 0

for letra in frase:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        count+=1

print("A quantidade de vogais é:", count)