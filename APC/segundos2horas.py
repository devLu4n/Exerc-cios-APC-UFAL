seg = int(input("Digite seu valor em segundos: "))
horas = seg//3600
min = (seg%3600) // 60
segundos = (min%60)
print("Seu tempo total é de: ", horas, "hora(s)", min, "minuto(s) e", segundos, "segundos")