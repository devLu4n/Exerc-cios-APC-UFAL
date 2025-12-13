taxisx = [21, 40, 35, 17, -42, 82, 60, -1, -15, 25, 29, 0]
taxisy = [25, 30, -1, 45, -20, 60, 0, 26, -10, 52, 36, -1]
x = 10
y = 8

menorD = 99999
i_menor = -1

for i in range(len(taxisx)):
    distancia = (((taxisx[i]- x)**2) + ((taxisy[i]-y)**2))**0.5

    if distancia < menorD:
        menorD = distancia
        i_menor = i

print(i_menor)