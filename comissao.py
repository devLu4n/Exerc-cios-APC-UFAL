venda = float(input("Digite o valor total de venda: "))

if venda < 30000:
    print(venda*1.07)
elif 30000 <= venda < 50000:
    print(venda*1.095)
elif venda >= 50000:
    print(venda*1.12)