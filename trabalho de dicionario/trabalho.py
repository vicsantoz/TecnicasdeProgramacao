from time import perf_counter

def removerSimbolos(texto):
    novo_texto = ""
    for letra in texto:
        if letra.isalpha():
            novo_texto += letra
        else:
            novo_texto += " "
    return novo_texto

def selecionarPalavras(texto):
    texto = removerSimbolos(texto)
    texto = texto.lower()
    palavras = texto.split()
    return palavras

def carregarPalavrasArquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    lista_palavras = selecionarPalavras(conteudo)
    return lista_palavras

def frequenciaPalavrasDicionario(lista_palavras):
    dic_freq = {}
    for palavra in lista_palavras:
        if palavra in dic_freq:
            dic_freq[palavra] += 1
        else:
            dic_freq[palavra] = 1
    return dic_freq


nome_arquivo = "alice29.txt"
print("Lendo o arquivo e preparando as palavras...")
palavras = carregarPalavrasArquivo(nome_arquivo)

print("Contando as palavras, isso pode levar um tempinho...")
inicio = perf_counter()
frequencias = frequenciaPalavrasDicionario(palavras)
fim = perf_counter()

tempo = fim - inicio
print(f"\nTempo de contagem: {tempo:.4f} segundos")

print("\nExemplos de frequência:")
print(f"Alice: {frequencias.get('alice', 0)} vezes")
print(f"Rabbit: {frequencias.get('rabbit', 0)} vezes")
print(f"Queen: {frequencias.get('queen', 0)} vezes")

with open("frequencia_palavras.txt", "w", encoding="utf-8") as saida:
    for palavra, freq in frequencias.items():
        saida.write(f"{palavra}: {freq}\n")

print("\nArquivo 'frequencia_palavras.txt' salvo com sucesso!")