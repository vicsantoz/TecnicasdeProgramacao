personagens = {
    "zangief": {"forca": 100, "vida": 150, "velocidade": 0, "magia": 0},
    "ken": {"forca": 50, "vida": 100, "velocidade": 50, "magia": 50},
    "ryu": {"forca": 75, "vida": 100, "velocidade": 50, "magia": 25},
    "chun-li": {"forca": 25, "vida": 75, "velocidade": 125, "magia": 50},
}

lutas = [
    {"p1": "ryu", "p2": "ryu", "venceu": "p1"},
    {"p1": "ken", "p2": "zangief", "venceu": "p2"},
    {"p1": "ken", "p2": "chun-li", "venceu": "p1"},
    {"p1": "ken", "p2": "ken", "venceu": "p2"},
    {"p1": "zangief", "p2": "zangief", "venceu": "p2"},
    {"p1": "ryu", "p2": "chun-li", "venceu": "p2"},
    {"p1": "chun-li", "p2": "chun-li", "venceu": "p1"},
]

#a)
print("Pontuação total de cada personagem: ")
for nome, stats in personagens.items():
    total = sum(stats.values())
    print(f"{nome}: {total}")

#b)
print("\nMédia geral das estatísticas: ")
for atributo in ["forca", "vida", "velocidade", "magia"]:
    media = sum(p[atributo] for p in personagens.values()) / len(personagens)
    print(f"{atributo}: {media:.1f}")

#c)
escolhas = {}
for luta in lutas:
    for p in [luta["p1"], luta["p2"]]:
        escolhas[p] = escolhas.get(p, 0) + 1

mais_escolhido = min([p for p, v in escolhas.items() if v == max(escolhas.values())])
print(f"\n Mais escolhido: {mais_escolhido} → {personagens[mais_escolhido]}")

#d)
vitorias = {}
for luta in lutas:
    vencedor = luta[luta["venceu"]]
    vitorias[vencedor] = vitorias.get(vencedor, 0) + 1

mais_vitorioso = min([p for p, v in vitorias.items() if v == max(vitorias.values())])
print(f"\n Mais vitorioso: {mais_vitorioso} → {personagens[mais_vitorioso]}")
