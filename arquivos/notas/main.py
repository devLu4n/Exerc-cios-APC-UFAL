#. Faça um programa que leia um número qualquer de notas em um arquivo. Após a leitura dos dados, faça o seguinte:
def contar(notas:list)-> int:
    return len(notas)
#Mostre a quantidade de notas que foram lidas.
#Exiba todas as notas na ordem em que foram informadas.
#Calcule e mostre a soma das notas.
def soma(notas:list)-> float:
    return sum(notas)
#Calcule e mostre a média das notas.
#Calcule e mostre a quantidade de notas acima da média calculada

if __name__ == "__main__":
    arquivo = open('dados/notas.txt')
