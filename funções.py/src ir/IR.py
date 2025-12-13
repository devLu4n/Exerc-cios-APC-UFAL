# Cálculo imposto de renda

def calcularImposto(salario: float) -> float:
	if salario <= 1500:
 		imposto = 0
    else:
	    imposto = 0.27*salario
	return imposto