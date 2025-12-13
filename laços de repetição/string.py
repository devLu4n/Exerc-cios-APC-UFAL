nome = (input("Digite seu nome: "))
soma = 0

for i in nome:
    if i=="a" or i=="A":
        soma += 1

print("A letra a aparece: ", soma, "vezes")
    