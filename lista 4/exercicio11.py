a, b = 1, 1
soma = a + b
for i in range(2, 20):
    a, b = b, a+b
    soma += b
print("Soma dos 20 primeiros termos da Fibonacci:", soma)
