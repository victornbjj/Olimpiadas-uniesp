







cafe = 3.00
cappuccino = 4.50
mocaccino = 5.00
chocolate_quente =4.00


print( "Digite 1 para café")
print( "Digite 2 para Cappuccino")
print( "Digite 3 para Mocaccino")
print( "Digite 4 para Chocolate Quente")



menu = int(input("Digite uma opcao do menu: "))




if menu == 1:
    saldo = float(input("Digite o valor: "))
    if saldo < cafe:
        print ("Valor insuficiente!")
    else:
        print ("Café")
        print (f"Troco {saldo - cafe:.2f}")
elif menu == 2:
    saldo = float(input("Digite o valor: "))
    if saldo < cappuccino:
        print ("Valor insuficiente!")
    else:
        print ("Cappuccino")
        print (f"Troco {saldo - cappuccino:.2f}")
elif menu == 3:
    saldo = float(input("Digite o valor: "))
    if saldo < mocaccino:
        print ("Valor insuficiente!")
    else:
        print ("Mocaccino")
        print (f"Troco {saldo - mocaccino:.2f}")
elif menu == 4:
    saldo = float(input("Digite o valor: "))
    if saldo < chocolate_quente:
        print ("Valor insuficiente!")
    else:
        print ("Chocolate Quente")
        print (f"Troco {saldo - chocolate_quente:.2f}")

else: 
    print ("Código inválido!")