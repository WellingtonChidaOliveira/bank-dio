from account import Account 
from user import User 
users = {}
accounts = {}

def get_input(prompt):
    return input(prompt)

def create_user():
    cpf = get_input("Type your cpf: ")
    if cpf in users:
        print("User already exists")
        return
    name = get_input("Type name: ")
    age = get_input("Type age: ")
    user = User(name, cpf, age)
    users[cpf] = user
    create_account(user)

def create_account(user):
    account = Account(user)
    accounts[user.cpf] = account

def access_account():
    cpf = get_input("Type your cpf: ")
    if cpf in users:
        account = accounts[cpf]
        operations = {
            '1': account.withdrawn,
            '2': account.deposit,
            '3': account.extract,
            '4': exit
        }
        while True:
            print("""
            1 - withdrawn
            2 - deposit
            3 - extract
            4 - exit
            """)
            choice = get_input("Type operation: ")
            operation = operations.get(choice)
            if operation:
                operation()
            else:
                print("Invalid option")
    else:
        print("User not found")

choice_actions = {
    '0': exit,
    '1': create_user,
    '2': access_account
}

while True:
    print("""
    Welcome to the bank
    Type the option:
    0 - exit
    1 - create account
    2 - access account
    """)
    choice = get_input("Type your choice: ")
    action = choice_actions.get(choice)
    if action:
        action()
    else:
        print("Invalid operation")