class Calculator:

    def __init__(self):   
        self.value1 = 0          
        self.value2 = 0

    def Accept(self):      
        print("Enter first number :")
        self.value1 = int(input())

        print("Enter second number :")
        self.value2 = int(input())

    def Add(self):      
        return self.value1 + self.value2

    def Substract(self):
        if(self.value1 > self.value2):
            return self.value1 - self.value2
        else:
            return self.value2 - self.value1

    def Multiply(self):
        return self.value1 * self.value2

    def Divide(self):
        return self.value1 / self.value2

def main():
    obj1 = Calculator()
    obj2 = Calculator()
    obj3 = Calculator()
    obj1.Accept()
    print(obj1.Add())
    print(obj1.Substract())
    print(obj1.Multiply())
    print(obj1.Divide())
    obj2.Accept()
    print(obj2.Add())
    print(obj2.Substract())
    print(obj2.Multiply())
    print(obj2.Divide())
    obj3.Accept()
    print(obj3.Add())
    print(obj3.Substract())
    print(obj3.Multiply())
    print(obj3.Divide())

if __name__ == "__main__":
    main()