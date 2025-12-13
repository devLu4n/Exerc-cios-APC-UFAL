valor = "1899832689113815687997165"

valor_mask = valor[:3]
print(len(valor))
total = len(valor)-6
for i in range(total):
    valor_mask += "*"
valor_mask += valor[-3:]
print(valor_mask)