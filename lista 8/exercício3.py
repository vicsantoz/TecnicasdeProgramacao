frase = input("Digite uma frase: ")

contagem = {}

for caractere in frase:
    contagem[caractere] = contagem.get(caractere, 0) + 1

print("\nContagem de caracteres:")
for chave, valor in contagem.items():
    print(f"'{chave}': {valor}")
