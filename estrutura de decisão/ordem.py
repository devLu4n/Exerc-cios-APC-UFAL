i = int(input("Digite o 1° número: "))
i2 = int(input("Digite o 2° número: "))
i3 = int(input("Digite o 3° número: "))

if i <= i2 and i <= i3:
    if i2 <= i3:
        print(i, i2, i3)
    else:
        print(i, i3, i2)
elif i2 <= i and i2 <= i3:
    if i <= i3:
        print(i2, i, i3)
    else:
        print(i2, i3, i)
else:
    if i <= i2:
        print(i3, i, i2)
    else:
        print(i3, i2, i)
