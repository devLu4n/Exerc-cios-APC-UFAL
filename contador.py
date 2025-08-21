min= 1
max = 100
quant_par = 0

for x in range(min, max+1):
    if x!=0 and x%2==0:
        quant_par +=1
        #quant_par = quant_par+1
        
print("A quantidade de pares é: ", quant_par)