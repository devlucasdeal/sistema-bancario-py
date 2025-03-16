menu = """
=====MENU=====
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Escolha a opção Desejada: 
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    resposta_menu = input(menu)

    if resposta_menu == "d":
        valor_deposito = float(input("Insira o valor do seu depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
            print(extrato)
            print(f"Seu saldo é de: R$ {saldo:.2f}")

        elif valor_deposito <= 0:
            print("Operação falhou! Valores negativos não podem ser depositados.")

        else:
            print("Operação falhou! Valor informado não permitido.")

    elif resposta_menu == "s":
        valor = float(input("Digite o valor que deseja sacar: "))

        excedeu_saque = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saque:
            print("Operação falhou! Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o seu limite diario!")

        elif excedeu_saques:
            print("Operação falhou! Você excedeu o número de saques diario!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques = 1
            print(extrato)
            print("Saque realizado! Retire suas notas.")

        else:
            print("Operação falhou! O valor informado é invalido!")            

    elif resposta_menu == "e":
        print("\n==========EXTRATO==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================")

    elif resposta_menu == "q":
        break

    else:
        print("Operação inválida, por favor seleciona novamente a operação desejada.")