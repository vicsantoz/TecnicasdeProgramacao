ap = float(input("Altura da parede m: "))
lp = float(input("Largura da parede m: "))
aa = float(input("Altura do azulejo m: "))
la = float(input("Largura do azulejo m: "))

area_parede = ap * lp
area_azulejo = aa * la
quantidade = area_parede / area_azulejo

print(f"Quantidade de azulejos necessária: {quantidade:.0f}")
