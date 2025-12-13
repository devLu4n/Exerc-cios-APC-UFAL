contatos = []
continuar = "s"

while continuar == "s":
    nome = input("Digite um nome: ")
    contatos.append(nome)
    continuar = input("Deseja adicionar mais um contato? (s/n): ")

print(contatos)

cont1 = input("Digite o nome do contato que deseja buscar: ")
i = 0
while i < len(contatos) and contatos[i] != cont1:
    i += 1
    if i == len(contatos):
        print("Contato não encontrado.")
    else:
        print("Contato encontrado:", contatos[i], i)
