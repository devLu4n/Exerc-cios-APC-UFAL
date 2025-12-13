taxisx = [21, 40, 35, 17, -42, 82, 60, -1, -15, 25, 29, 0]
taxisy = [25, 30, -1, 45, -20, 60, 0, 26, -10, 52, 36, -1]
x = 10
y=8

menor_d= 99999999999999999999999
i_prox = -1

for i in range(len(taxisx)):
    distancia = (((taxisx[i]-x)**2)+((taxisy[i]- y)**2))**0.5

    if distancia < menor_d:
        menor_d = distancia
        i_prox = i

print(i_prox)