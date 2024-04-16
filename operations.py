def withdrawn(balance: float, hist: str, withdrawn: float):
    value= float(input("Digite o valor a ser sacado: "))
    if balance < value or value > 500 or withdrawn + value > 500:
        print("Saldo insuficiente, valor acima do permitido ou limite diário atingido")
        hist += f"valor:{value} operação: saque negado\n"
    else:
        balance -= value
        withdrawn += value
        hist += f"valor:{value} operação: saque\n"
    return balance, hist, withdrawn

def deposit(balance: float, hist: str):
    value = float(input("Digite o valor a ser depositado: "))
    balance += value 
    hist += f"value:{value} operação: deposito\n"
    return balance, hist

def extract(hist: str):
    print(hist)