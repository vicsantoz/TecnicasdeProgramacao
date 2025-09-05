morangos = float(input("Kg de morangos: "))
macas = float(input("Kg de maçãs: "))

if morangos < 5:
    preco_morango = 22
else:
    preco_morango = 20

if macas < 5:
    preco_maca = 6
else:
    preco_maca = 5

total_kg = morangos + macas
total_preco = (morangos * preco_morango) + (macas * preco_maca)

if total_kg > 8 or total_preco > 100:
    total_preco *= 0.9  # desconto 10%

print(f"Total de Kg: {total_kg}")
print(f"Valor a pagar: R$ {total_preco:.2f}")