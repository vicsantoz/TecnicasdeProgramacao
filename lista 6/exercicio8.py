idades = [int(input(f"Digite a idade do aluno {i+1}: ")) for i in range(30)]
media = sum(idades) / len(idades)
quantidade = sum(1 for idade in idades if idade < 13 and idade > media)
print(f"Quantidade de alunos com menos de 13 anos e idade superior à média: {quantidade}")