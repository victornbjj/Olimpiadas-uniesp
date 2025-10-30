# Seu programa deve ler um número inteiro N e imprimir o triângulo conforme o padrão
# acima.

# Entrada
# Um único número inteiro N (1 ≤ N ≤ 50), representando a altura do triângulo.

# Saída
# O triângulo de números, com cada linha iniciando em 1 até o número da linha e os
# números separados por um espaço.


try:
    N = int(input("Digite um número inteiro N para a altura do triângulo: "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
    exit()


if N <= 0:
    print("N deve ser um número inteiro positivo.")
else:
    
    for i in range(1, N + 1):
       
        linha_atual = ""

        
        for j in range(1, i + 1):
            
            linha_atual += str(j)

            
            if j < i:
                linha_atual += " "

       
        print(linha_atual)
