numeros = [3,5,6,7,12,9,43,11,42]
n = 10
mais_proxim = abs(n - numeros[0])
mais_proxim2= None

if len(numeros) == 0:
    print("A lista está vazia.")
else:
    for i in numeros[1:]:
        diferenca = abs(n - i)
        if diferenca < abs(n - mais_proxim):
            mais_proxim = i
        elif diferenca == abs(n - mais_proxim) and i != mais_proxim:
                mais_proxim2 = i

print("O número mais próximo de", n, "é", mais_proxim, "e o segundo mais próximo é", mais_proxim2)