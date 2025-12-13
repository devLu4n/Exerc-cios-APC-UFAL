import hashlib

def encriptar(texto):
    hash_obj = hashlib.sha256()
    hash_obj.update(texto.encode('utf-8'))
    hash_hex = hash_obj.hexdigest()
    return hash_hex

arquivo_entrada = open('usuarios.csv', 'r')
linhas = arquivo_entrada.readlines()
arquivo_entrada.close()

arquivo_saida = open('usuarios_criptografados.csv', 'w')

cabecalho = linhas[0]
arquivo_saida.write(cabecalho)

for i in range(1, len(linhas)):
    linha = linhas[i].strip() 
    if linha: 
        partes = linha.split(',')
        
        nome = partes[0]
        email = partes[1]
        senha = partes[2]
        
        senha_criptografada = encriptar(senha)
        
        nova_linha = nome + ',' + email + ',' + senha_criptografada + '\n'
        arquivo_saida.write(nova_linha)

arquivo_saida.close()
print("Pronto! Arquivo 'usuarios_criptografados.csv' criado com sucesso!")