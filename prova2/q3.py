notas = [2,5,8,9,6,4,7]
notamin = notas[0]
notamax = notas[0]
maior = 10
menor = 0
novas_notas = []
nota_calculada = []
for i in notas:
    if i > notamax:
       notamax = i
    if i < notamin:
       notamin= i

print(notamin, notamax)
for i in notas:
    if i> menor and i<maior:
       notanorm = ((i-notamin)/(notamax -notamin)) * 10
       nota_calculada = notanorm
       novas_notas.append(nota_calculada)
    elif i == notamax:
        notamax = maior
        novas_notas.append(notamax)
    elif i == notamin:
        notamin = menor
        novas_notas.append(notamin)
    
print("As novas notas calculadas são: ",novas_notas)