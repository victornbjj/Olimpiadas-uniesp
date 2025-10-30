# Marina gosta de estudar números primos. Ela quer descobrir quantos números primos
# existem em uma sequência de números inteiros positivos.
# O usuário digita vários números inteiros positivos, um por linha. A sequência termina
# quando for digitado o número 0.
# O programa deve contar quantos números da sequência são primos.
# Lembre-se: Um número é primo se for maior que 1 e só for divisível por 1 e ele mesmo.
    
# Uma sequência de números inteiros positivos, um por linha.
# A sequência termina quando o usuário digitar 0.

# Um único número inteiro: a quantidade de números primos na sequência.


numeros = []

contador_primos = 0
while True:
    usuario = int(input("digite um numero:"))
    if usuario == 0:
        break
    else:
        numeros.append(usuario)
for numero in numeros:
    eh_primo = True
    
    # 1. Regra base para primos
    if numero <= 1:
        eh_primo = False
    
    # 2. Loop de verificação de divisores (só executa se for > 1)
    if eh_primo:
        for divisor in range(2, numero): 
            if numero % divisor == 0:
                eh_primo = False
                break  
    
    # 3. CONTAGEM: Este bloco DEVE estar dentro do for
    # Se a flag for True (o número é primo), incrementa o contador
    if eh_primo:
        contador_primos += 1
print(contador_primos)