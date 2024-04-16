import operations
users = {}
accounts = {}

def create_user():
    cpf = input("Digite seu cpf: ")
    if cpf in users:
        print("Usuário já cadastrado")
        return
    user = {
        'name': input("Digite seu nome: "),
        'cpf': cpf,
        'idade': input("Digite sua idade: ")
    }
    users[cpf] = user
    create_account(cpf)

def create_account(cpf):
    account = {
        'user': users[cpf],
        'agency': '0001',
        'balance': 0,
        'hist': f"valor:{0} operação: inicialização\n",
        'withdrawn': 0
    }
    accounts[cpf] = account



def access_account():
    
    cpf = input("Digite seu cpf: ")
    if cpf in users:
        account = accounts[cpf]
        print(
            """
            1 - sacar
            2 - deposit
            3 - extrato
            4 - sair
            """
        )
        choice = input("Digite a opção desejada: ")
        while choice != '4':
            if choice == '1':
               account['balance'], account['hist'], account['withdrawn'] = operations.withdrawn(balance=account['balance'], hist=account['hist'], withdrawn=account['withdrawn'])
            elif choice == '2':
               account['balance'], account['hist'] = operations.deposit(balance= account['balance'], hist= account['hist'])
            elif choice == '3':
                operations.extract(hist= account['hist'])
            else:
                print("Opção inválida")
            choice = input("Digite a opção desejada: ")
        print("Obrigado por usar nosso banco")
    else:
        print("Usuário não encontrado")
        


choice_actions = {
    '0': exit,
    '1': create_user,
    '2': access_account
}

while True:
    print("""
    Bem vindo ao banco
    Digite a opção desejada
    0 - sair
    1 - criar conta
    2 - acessar conta
    """)

    choice = input("Digite a opção desejada: ")
    action = choice_actions.get(choice)

    if action:
        action()
    else:
        print("Opção inválida")
