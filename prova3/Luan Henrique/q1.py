def autenticar(email, senha):
    for usuario in usuarios:
        if usuario["email"] == email:
            if usuario["senha"] == senha:
                return "Autenticado"
            else:
                return "Não autenticado"
    return "Não autenticado"

usuarios = [
    {"nome": "Ana", "email": "ana@gmail.com", "senha": "ana123"},
    {"nome": "Bob", "email": "bob@hotmail.com", "senha": "123bob"},
    {"nome": "Claudio", "email": "claudio@bol.com", "senha": "clau!*"}
]

print(autenticar("bob@hotmail.com", "123bob"))          
print(autenticar("claudio@bol.com", "123claudio"))   
print(autenticar("luan123@gmail.com", "abc12345."))
