produtos = [
    {
        "nome": "maquina de lavar",
        "valor": 1350.0,
        "quantidade": 12,
        "comentarios": ["bacana", "veio arranhada", "gasta muita energia"],
        "notas": [1, 1, 1, 3, 5, 1, 1, 2, 1, 1],
    },
    {
        "nome": "placa de video",
        "valor": 15732.99,
        "quantidade": 3,
        "comentarios": ["top", "tem raytracing", "muito rapida", "barulhenta", "esquenta bastante"],
        "notas": [5, 5, 5, 5, 5, 4, 5, 4, 4, 5, 5],
    },
    {
        "nome": "biografia - ozzy osbourne",
        "valor": 9.99,
        "quantidade": 30,
        "comentarios": ["bem maluco", "um monstro sagrado do rock"],
        "notas": [5, 1, 3, 4, 5, 5],
    },
    {
        "nome": "geladeira frost free",
        "valor": 2469.50,
        "quantidade": 4,
        "comentarios": ["gostei", "maior do que esperava", "linda", "nao produz gelo :O"],
        "notas": [4, 4, 5, 3, 3, 3, 4, 5, 1, 0],
    },
]

#a)
print("Quantidade de produtos: ", len(produtos))

#b)
for p in produtos:
    media = sum(p["notas"]) / len(p["notas"])
    print(f"\n{p['nome']}")
    print("Comentários: ", len(p["comentarios"]))
    print("Média das notas: ", round(media, 2))

#c)
print("\n Último comentário de cada produto: ")
for p in produtos:
    print(p["nome"], "→", p["comentarios"][-1])

#d)
p3 = produtos[2]
print(f"\n 3º produto: {p3['nome']} - Estoque: {p3['quantidade']}")

#e)
todas_notas = [nota for p in produtos for nota in p["notas"]]
media_geral = sum(todas_notas) / len(todas_notas)
print("\nProdutos com nota média acima da média geral: ")
for p in produtos:
    media = sum(p["notas"]) / len(p["notas"])
    if media > media_geral:
        print(p["nome"])

#f)
for p in produtos:
    p["valor"] *= 0.9
print("\n Preços atualizados (10% de desconto):")
for p in produtos:
    print(p["nome"], "→ R$", round(p["valor"], 2))

#g)
produtos[3]["quantidade"] -= 1
print(f"\n Após venda: {produtos[3]['nome']} agora tem {produtos[3]['quantidade']} unidades.")
