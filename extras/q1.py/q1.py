nota1 = float(input("Digite a nota:"))


media = nota1 

if media >= 7:
    situacao = "Aprovado"
elif media >= 5 and media <= 6.9:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(situacao)