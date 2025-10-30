# Carlos está praticando matemática e quer somar uma sequência de números positivos.
# Ele digita vários números inteiros positivos, um por vez. O programa deve calcular a soma
# de todos os números positivos até que ele digite um número zero ou negativo, que indica
# o fim da sequência.

# Entrada
# Uma sequência de números inteiros, um por linha.
# A sequência termina quando o usuário digitar um número ≤ 0.

# Saída
# Um único número inteiro, representando a soma de todos os números positivos digitados antes do número zero ou negativo.


numeros = []
while True:
    usuario = int(input("digite um numero:"))
    if usuario <= 0:
        break
    else:
        numeros.append(usuario)

1
total_numeros = sum(numeros)
print (total_numeros)