print("-----------------------------WELCOME TO WEST NAT-----------------------------")
print("                            Online banking system                            ")
print("START BY ENTERING DETAILS DONE SO: JACK = bank('Jack', 14, 'male'")
print("To view details do: Jack.show_user_details()")
print("To make a deposit do: Jack.deposit(100) ")
print("To withdraw do: Jack.withdraw(50)")
print("Note name and amount of money is just and example it can be whatever")
#parent class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print("Personall details")
        print("")
        print("Name : ", self.name)
        print("age : ", self.age)
        print("gender ", self.gender)

#child class
class bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.total = 0

    def deposit(self,amount):
        self.amount = amount
        self.total = self.total + self.amount
        print("Account balance is updated : £", self.total)

    def withdraw(self,amount):
        self.amount = amount
        if(self.amount > self.total):
            print("insufficient funds Balance Avaliable : £", self.total)
        else:
            self.total = self.total - self.amount
            print("Your balance has been updated : £", self.total)
    def veiw_balance(self):
        self.show_user_details()
        print("Your total balance is : £", self.total)
        
