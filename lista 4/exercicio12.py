altura_jequitiba = 1.50
altura_jaqueira = 1.10
altura_jabuticabeira = 2.98

for i in range(25):
    altura_jequitiba += 0.01
    altura_jaqueira += 0.02

maior = max(altura_jequitiba, altura_jaqueira, altura_jabuticabeira)
print("Maior altura após 25 anos:", maior)