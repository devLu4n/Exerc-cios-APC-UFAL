cript = input("Digite sua mensagem:")

# Encrypt the message by shifting each character by 3
cript_encrypted = ""
for i in cript:
    cript_encrypted += chr(ord(i) + 3)

print(cript_encrypted)

# Decrypt the message by shifting each character back by 3
cript_decrypted = ""
for i in cript_encrypted:
    cript_decrypted += chr(ord(i) - 3)
print(cript_decrypted)
