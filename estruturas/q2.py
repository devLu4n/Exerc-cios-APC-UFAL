def media(notas, nome):
    return sum(notas[nome]) / 2

notas = {}

while True:
    nome = input("Nome do aluno (vazio para sair): ")
    if nome == "":
        break
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    notas[nome] = [n1, n2]

nome_busca = input("Consultar média de qual aluno? ")
if nome_busca in notas:
    print(f"Média de {nome_busca}: {media(notas, nome_busca):.2f}")
else:
    print("Aluno não encontrado.")


