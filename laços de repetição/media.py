lista = [2,4, 9,5,6, 10, 12, 15]
count = 0
media = 9

for i in lista:
    if i < media:
        count+=1

print("números abaixo da média são:", count)