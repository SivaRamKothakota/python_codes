class Account:
    # constructor
    def __init__(self, acno, ahname, balance=0):
        # Attributes
        self.acno = acno
        self.ahname = ahname
        # private attribute
        self.__balance = balance
        #print(acno)
    # Methods
    def deposit(self , amount):
       self.__balance += amount

    def getbalance(self):
        return self.__balance

    def show(self):
        print("Acno     : ", self.acno)
        print("Ahname   : ", self.ahname)
        print("Balance  : ", self.__balance)


a1 = Account(1, "Scott")  # Create an object/instance
a1.deposit(10000)
a1.deposit(20000)
#print(a1.__dict__)
#print(a1.balance)
#print(a1._Account__balance)

# a1.show()

a2 = Account(2, "Mark", 50000)
# a2.show()