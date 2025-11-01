texto = input("Digite um texto: ").lower()
vogais = "aeiou"

contagem = {}

for v in vogais:
    contagem[v] = texto.count(v)

print("\n Quantidade de vogais no texto:")
print(contagem)
