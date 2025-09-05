tipo = input("Tipo de combustível (A-álcool, G-gasolina): ").upper()
litros = float(input("Litros vendidos: "))
preco = float(input("Preço por litro: "))

if tipo == "A":
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
elif tipo == "G":
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
else:
    desconto = 0

valor_total = litros * preco * (1 - desconto)
print(f"Valor a pagar: R$ {valor_total:.2f}")
