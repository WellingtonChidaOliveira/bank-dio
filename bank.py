import operations

print(
    """
    1 - sacar
    2 - deposit
    3 - extrato
    4 - sair
    """
)

choice = input("Digite a opção desejada: ")

balance = 0
hist = f"valor:{balance} operação: inicialização\n"
withdrawn = 0

while choice != '4':
    if choice == '1':
         balance, hist, withdrawn = operations.withdrawn(balance=balance, hist=hist, withdrawn=withdrawn)
    elif choice == '2':
        balance, hist = operations.deposit(balance= balance, hist= hist)
    elif choice == '3':
        operations.extract(hist= hist)
    else:
        print("Opção inválida")
    
    choice = input("Digite a opção desejada: ")
    
print("Obrigado por usar nosso banco")