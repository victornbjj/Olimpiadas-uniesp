# Lúcia tem um gato chamado Fubá. Quando ela chega em casa, o comportamento de
# Fubá depende do horário:
# • Se for antes das 12 horas, ele está dormindo.
# • Se for entre 12 e 18 horas, ele está brincando.
# • Caso contrário (depois das 18 horas), ele está pedindo comida.
# Ajude Lúcia a descobrir o que Fubá está fazendo em determinado horário.




horario = int(input("Digite um horario: "))

if horario < 12: 
    print("Dormindo")
elif horario > 12 and horario <= 18:
    print("Brincando")
elif horario > 18:
    print("Pedindo comida")

