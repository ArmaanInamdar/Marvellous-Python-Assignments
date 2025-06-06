class Arithematic:

    def __init__(self):   
        self.value1 = 0          
        self.value2 = 0

    def Accept(self):      
        print("Enter first number :")
        self.value1 = int(input())

        print("Enter second number :")
        self.value2 = int(input())

    def Addition(self):      
        return self.value1 + self.value2

    def Substraction(self):
        if(self.value1 > self.value2):
            return self.value1 - self.value2
        else:
            return self.value2 - self.value1

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        return self.value1 / self.value2

def main():
    obj1 = Arithematic()
    obj2 = Arithematic()
    obj3 = Arithematic()
    obj1.Accept()
    print(obj1.Addition())
    print(obj1.Substraction())
    print(obj1.Multiplication())
    print(obj1.Division())
    obj2.Accept()
    print(obj2.Addition())
    print(obj2.Substraction())
    print(obj2.Multiplication())
    print(obj2.Division())
    obj3.Accept()
    print(obj3.Addition())
    print(obj3.Substraction())
    print(obj3.Multiplication())
    print(obj3.Division())

if __name__ == "__main__":
    main()