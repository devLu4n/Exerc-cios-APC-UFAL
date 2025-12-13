def ir(funcionarios):
    for funcionario in funcionarios:
        if 'salario' in funcionario:
            salario = funcionario['salario']
        else:
            salario = 0

        if 'comissao' in funcionario:
            comissao = funcionario['comissao']
        else:
            comissao = 0

        imposto = 0.27 * (salario + comissao)

        funcionario['salario_liquido'] = (salario + comissao) - imposto
        funcionario['imposto'] = round(imposto, 2)

    return funcionarios

dados = [
    {'nome': 'ana', 'cpf': '2344456878', 'salario': 1580},
    {'nome': 'pedro', 'cpf': '04458712365', 'salario': 3240.32, 'comissao': 250},
    {'nome': 'beto', 'cpf': '78945625865', 'salario': 1852.20, 'comissao': 350}
]

resultado = ir(dados)
print(resultado)