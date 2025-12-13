def tipo(num:int):
    if num%2== 0:
        return "Par"
    else:
        return "Ímpar"
    
num = int(input("Digite um número: "))
print(tipo(num))