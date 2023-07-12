Menu = """

(D) Depositar

(S) Sacar

(E) Extrato

(L) Sair

=> """

Saldo = 1500
Limite = 500
Extrato = ""
Numero_Saque = 0

while True:
    opcao = input(Menu)

    if opcao == "D":
        Valor = float(input("Informe o valor do depósito: "))
        
        if Valor > 0: 
         Saldo += Valor
         Extrato += f"Deposito: R$ {Valor:.2f}\n"
        
        else:
         print("Erro de operacao, digite um valor valido.")
       
    elif opcao == "S":
        Valor = float(input("informe o valor do saque: "))

        Test_Saldo = Valor > Saldo
        Test_Limite = Valor > Limite
        Test_Saque = Numero_Saque >= 3

        if Test_Saldo:
            print("Erro de operacao, saldo insuficiente.")
            
        elif Test_Limite: 
            print("Erro de operacao, limite exedido.")

        elif Test_Saque: 
            print("Erro de operacao, Saque exedido.")

        elif Valor > 0:
            Saldo -= Valor
            Extrato += f"saque: R$: {Valor:.2}\n"
            Numero_Saque  += 1

        else:
         print("Erro de operacao, digite um valor valido.")

    elif opcao == "E":
        print("\n========== Extrato ==========")
        print("Nao foi realizado movimentacao na conta" if not Extrato else Extrato )
        print(f"\n Saldo: R$: {Saldo:.2f}")
        print("\n=============================")

    elif opcao =="L":     
       break

    else:
       print("Erro de operacao, elscolha uma opcao valida")


    