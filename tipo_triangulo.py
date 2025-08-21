a = int(input("Digite o lado a do triângulo: "))
b = int(input("Digite o lado b do triângulo: "))
c = int(input("Digite o lado c do triângulo: "))

if ((a< (b+c)) and (b < (a+b)) and (c < (a+b))):
    if (a != b != c):
        print("O triângulo é escaleno")
    elif (a == b == c):
        print("O triângulo é equilátero")
    else: 
        print("O triângulo é isósceles")