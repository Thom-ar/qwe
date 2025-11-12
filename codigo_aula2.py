import random
elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamanho = int(input("Digite o tamanho da senha: "))
senha = ""
for i in range(tamanho):
    senha += random.choice(elementos)
print("Senha gerada:", senha)