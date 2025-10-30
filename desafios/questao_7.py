# Carlos está aprendendo a programar e quer analisar uma sequência de números
# inteiros.
# Ele precisa de um programa que faça o seguinte:
# 1. Leia N números inteiros e armazene-os em um vetor.
# 2. Calcule a média dos números.
# 3. Determine o maior valor do vetor.
# O programa deve então imprimir a média arredondada para duas casas decimais e o
# maior valor.



# Entrada
# • A primeira linha contém um inteiro N (1 ≤ N ≤ 100), representando a
# quantidade de números.
# • A segunda linha contém N números inteiros separados por espaço.


# Duas linhas:
# 1. "Média: X.XX" — a média dos números, com duas casas decimais.
# 2. "Maior: Y" — o maior número do vetor.

numeros = []
usuario = int(input())
for i in range (usuario):
    n = int(input())
    numeros.append(n)


tamanho = len(numeros)
maior_valor = max(numeros)
total_numeros = sum(numeros)
media = total_numeros / tamanho


print (f"Média: {media:.2f}")
print (f"Maior: {maior_valor}")
