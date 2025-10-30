# Joana está estudando padrões em sequências de números. Ela quer um programa que,
# dado um vetor de números inteiros, conte quantos números aparecem mais de uma
# vez.
# Por exemplo, na sequência [2, 3, 2, 5, 3], os números 2 e 3 aparecem mais de uma vez,
# totalizando 2 números repetidos.
# O programa deve ler os números, armazená-los em um vetor, e calcular quantos
# números distintos se repetem.

# • A primeira linha contém um inteiro N (1 ≤ N ≤ 100), representando a
# quantidade de números.
# • A segunda linha contém N números inteiros separados por espaço.


# • Um único número inteiro: a quantidade de números distintos que aparecem
# mais de uma vez.

numeros = []
repedidos=  []
vistos = []
usuario = int(input())
for i in range (usuario):
    n = int(input())
    numeros.append(n)

for numero in numeros:
    if numero not in vistos:
        vistos.append(numero)
    elif numero in vistos and numero not in repedidos:
        repedidos.append(numero)
    else:
        continue 
quantidade_repetida = len(repedidos)
print(quantidade_repetida)



    
