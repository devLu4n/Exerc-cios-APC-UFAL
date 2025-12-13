def sistema():
   alunos = {}
   while True:
    while nome!= "":
     nome = input("Digite o nome do aluno")
     ab1 = int(input("Digite a primeira nota:"))
     ab2 = int(input("Digite a segunda nota:"))
     alunos[nome] = [ab1, ab2]
    return alunos
   
def media(alunos, nome):
  if nome in alunos:
    return sum(alunos[nome]) / len(alunos[nome])    
  else: return None
   
notas_alunos = sistema()
nome_pesquisa = input("Consultar média de qual aluno? ").strip() #strip remove espaços
mediaA = media(notas_alunos, nome_pesquisa)
if mediaA is not None:
    print(f"Média de {nome_pesquisa}: {media:.2f}")
else:
    print("Aluno não encontrado.")

    
   