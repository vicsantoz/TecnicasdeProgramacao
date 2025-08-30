hi = int(input("Hora inicial: "))
mi = int(input("Minuto inicial: "))
hf = int(input("Hora final: "))
mf = int(input("Minuto final: "))

if 0 <= hi < 24 and 0 <= hf < 24 and 0 <= mi < 60 and 0 <= mf < 60:
    inicio = hi*60 + mi
    fim = hf*60 + mf
    if fim <= inicio:
        fim += 24*60
    duracao = fim - inicio
    horas = duracao // 60
    minutos = duracao % 60
    print(f"Duração do jogo: {horas} hora(s) e {minutos} minuto(s)")
else:
    print("Entrada de dados não é válida.")