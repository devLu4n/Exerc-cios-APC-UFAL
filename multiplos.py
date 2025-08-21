A = int(input("Digite um valor A:"))
B = int(input("Digite um valor B:"))

if A % B == 0 or B % A == 0:
    multiplos = "Verdade" 
else: 
    multiplos = "Falso"

print("Os números são múltiplos?:", multiplos)