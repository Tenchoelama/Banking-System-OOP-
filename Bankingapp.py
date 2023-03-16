
#Parent Class
class User():
    
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print(f"{self.name} details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        
#Child Class
class Bank(User):
    
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
        
    def deposit(self, amount):
        self.amount = amount 
        self.balance = self.balance + amount 
        print("Account balance has been updated: $", self.balance)
        
    def withdraw(self, amount):
        self.amount = amount 
        if self.amount > self.balance:
            print('Insufficient funds! | Balance available: $', self.balance) 
            
        else:
            self.balance = self.balance - amount
            print("Account balance has been updated: $", self.balance)
            
    def view_balance(self):
        self.show_details()
        print("Account balance: $", self.balance)

# Tenzin = Bank('Tenzin', 24, 'Male')
# Tenzin.show_details()
# Tenzin.deposit(100)
# Tenzin.withdraw(200)
# Tenzin.view_balance()

        
        

    
    

