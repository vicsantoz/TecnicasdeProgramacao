sexo = input("Digite o sexo (M/F): ").upper()
idade = int(input("Digite a idade: "))

if (sexo == "M" and idade >= 21) or (sexo == "F" and idade >= 18):
    print("Maior de idade")
else:
    print("Menor de idade")