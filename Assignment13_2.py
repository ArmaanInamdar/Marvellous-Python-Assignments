class BankAccount:
    ROI = 10.5
    DepositAmount = 0

    def __init__(self,A):   
        self.Name = A          
        self.Amount = 0

    def Display(self):
        print("Name :"+self.Name)
        print("Amount :",BankAccount.DepositAmount)

    def Deposit(self):
        print("Enter to deposit :")
        self.Amount = int(input())
        BankAccount.DepositAmount = BankAccount.DepositAmount + self.Amount

    def Withdraw(self):
        print("Enter Amount to withdraw :")
        self.Amount = int(input())
        BankAccount.DepositAmount = BankAccount.DepositAmount - self.Amount

    def CalculateInterest(self):
        self.interest = self.Amount * BankAccount.ROI / 100



def main():
    print("Enter name")
    name1 = input()
    obj1 = BankAccount(name1)
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()
    obj1.Display()
    print("Enter name")
    name2 = input()
    obj2 = BankAccount(name2)
    obj2.Deposit()
    obj2.Withdraw()
    obj2.CalculateInterest()
    obj2.Display()
    
    

if __name__ == "__main__":
    main()