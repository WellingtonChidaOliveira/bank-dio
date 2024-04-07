def sacar(saldo: float, hist: str, total_sacado: float):
    valor= float(input("Digite o valor a ser sacado: "))
    if saldo < valor or valor > 500 or total_sacado + valor > 500:
        print("Saldo insuficiente, valor acima do permitido ou limite diário atingido")
        hist += f"valor:{valor} operação: saque negado\n"
    else:
        saldo -= valor
        total_sacado += valor
        hist += f"valor:{valor} operação: saque\n"
    return saldo, hist, total_sacado

def depositar(saldo: float, hist: str):
    valor = float(input("Digite o valor a ser depositado: "))
    saldo += valor 
    hist += f"valor:{valor} operação: deposito\n"
    return saldo, hist

def extrato(hist: str):
    print(hist)

print(
    """
    1 - sacar
    2 - depositar
    3 - extrato
    4 - sair
    """
)

choice = input("Digite a opção desejada: ")

saldo = 0
hist = f"valor:{saldo} operação: inicialização\n"
total_sacado = 0

while choice != '4':
    if choice == '1':
         saldo, hist, total_sacado = sacar(saldo=saldo, hist=hist, total_sacado=total_sacado)
    elif choice == '2':
        saldo, hist = depositar(saldo= saldo, hist= hist)
    elif choice == '3':
        extrato(hist= hist)
    else:
        print("Opção inválida")
    
    choice = input("Digite a opção desejada: ")