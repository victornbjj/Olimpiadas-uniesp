horario = int(input("Digite um horario: "))
fluxo = input("Digite o fluxo: ")
if fluxo.upper() == "A":
    if horario >= 6  and horario < 18:
     print("Tempo de sinal verde: 60 segundos")
    else:
     print("Tempo de sinal verde: 40 segundos ")
elif fluxo.upper() == "M":
    if horario >= 6  and horario < 18:
     print("Tempo de sinal verde: 40 segundos")
    else:
     print("Tempo de sinal verde: 25 segundos ")
elif fluxo.upper() == "B":
    if horario >= 6  and horario < 18:
     print("Tempo de sinal verde: 25 segundos. ")
    else:
     print("Tempo de sinal verde: 15 segundos ")

  






