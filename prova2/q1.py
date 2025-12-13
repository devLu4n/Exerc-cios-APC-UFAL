peso = [90, 90, 91, 90, 93, 90, 89, 90, 87, 90, 85, 91, 90, 90, 86]
count = -1

for i in peso:
    count +=1

    if i <88 or i> 92:
        print("Devem se descartar os itens:", count)
