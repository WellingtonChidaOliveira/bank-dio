import user 
class Account:
    def __init__(self, user, agency='0001'):
        self.user = user
        self._agency = agency
        self._balance = 0
        self._hist = f"valor:{0} operation: init\n"
        self._withdrawn = 0
        
    def __str__(self):
        return f"Usuário: {self.user['name']}, Agência: {self._agency}, Saldo: {self._balance}"
    
    def withdrawn(self):
        value = float(input("Type withdrawn value: "))
        if self._balance < value or value > 500 or self._withdrawn + value > 500:
            print("Insufficient amount, balance above the allow or daily limit hit")
            self._hist += f"balance:{value} operation: deny withdrawn\n"
        else:
            self._balance -= value
            self._withdrawn += value
            self._hist += f"balance:{value} operation: withdrawn\n"
        return self._balance, self._hist, self._withdrawn
    
    def deposit(self):
        value = float(input("Type value to deposit: "))
        self._balance += value 
        self._hist += f"Value:{value} operation: deposit\n"
        return self._balance, self._hist
    
    def extract(self):
        print(self._hist)