

from time import perf_counter   #para medir o tempo

#função para remover símbolos

def removerSimbolos(texto):
    resultado = ""
    #percorre cada caractere da string
    for caractere in texto:
        if caractere.isalpha():         #para letra
            resultado += caractere
        else:
            resultado += " "            #se não for letra vira espaço

    return resultado

#função para selecionar palavras

def selecionarPalavras(texto):
    texto_limpo = removerSimbolos(texto)  #função anterior
    texto_limpo = texto_limpo.lower()     #tudo minúsculo
    palavras = texto_limpo.split()        #quebra por espaços

    return palavras

#função para carregar palavras do arquivo

def carregarPalavrasArquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    return selecionarPalavras(texto)

#função que conta a frequência

def frequenciaPalavrasDicionario(lista_palavras):
    dicionario_frequencia = {}

    #percorre todas as palavras
    for palavra in lista_palavras:

        #verifica se já existe a palavra no dicionário
        if palavra in dicionario_frequencia:
            dicionario_frequencia[palavra] += 1   #soma 1
        else:
            dicionario_frequencia[palavra] = 1    #aparece pela primeira vez

    return dicionario_frequencia

#função principal

def main():
    print("carregando arquivo e preparando palavras")

    palavras = carregarPalavrasArquivo("alice29.txt")

    print("Total de palavras carregadas: ", len(palavras))

    #medir tempo da função do dicionário
    inicio = perf_counter()
    frequencias = frequenciaPalavrasDicionario(palavras)
    fim = perf_counter()

    tempo_total = fim - inicio

    print("\nTempo para contar as palavras: ")
    print(f"{tempo_total:.6f} segundos\n")

    print("Exemplos de frequências conhecidas:")
    print("alice →", frequencias.get("alice", 0))
    print("rabbit →", frequencias.get("rabbit", 0))
    print("queen →", frequencias.get("queen", 0))

    #salvar em arquivo
    with open("resultado_frequencia.txt", "w", encoding="utf-8") as arq:
        for palavra, freq in frequencias.items():
            arq.write(f"{palavra}: {freq}\n")

    print("\nArquivo 'resultado_frequencia.txt' salvo com sucesso!")

#roda o programa
if __name__ == "__main__":
    main()
