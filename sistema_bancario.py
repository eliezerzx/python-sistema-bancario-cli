# Criar conta
nome = input("Digite o seu nome: ")
saldoInicial = float(input("Digite seu saldo inicial: "))

saldo = saldoInicial
valorDepositado = 0

# Menu de opções
while True:
    print ("\n----------------------------------------------")
    print ("1 -- Depositar")
    print ("2 -- Ver saldo")
    print ("3 -- Sacar dinheiro")
    print ("4 -- Extrato bancario")
    print ("5 -- Sair")
    print ("----------------------------------------------")

    print ("\n********************************************")
    opcao = int(input("Escolha uma opcao:"))
    print ("\n********************************************")

    # Parte das variaveis com if, elif e else para cada opção do menu
    if opcao == 1:
        valorDepositado = float(input("Digite o valor que deseja depositar:"))
        saldo += valorDepositado

    elif opcao == 2:
        print (f"Valor do seu saldo: | {saldo:.2f} |")

    elif opcao == 3:
        valorSaque = float(input("Digite o valor que deseja sacar:"))

        if valorSaque <= saldo:
            saldo -= valorSaque
            print ("----------------------------------------------")
            print (f"Saque efetuado de \n  | R% {valorSaque:.2f} |")
            print ("----------------------------------------------")
        else:
            print ("----------------------------------------------")
            print("Saldo insuficiente!")
            print ("----------------------------------------------")

    elif opcao == 4:
        print("\n----------- EXTRATO ---------------------")
        print(f"Saldo atual     | R${saldo:.2f}")
        print(f"Ultimo deposito | R${valorDepositado:.2f}")
        print(f"Ultimo saque    | {valorSaque:.2f}")
        print ("-------------------------------------------")

    elif opcao == 5:
    # break para voltar para o menu de login
        break