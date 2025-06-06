class Demo:
    value = 0

    def __init__(self,A,B):   
        self.no1 = A           
        self.no2 = B  

    def Fun(self):      
        print(self.no1)
        print(self.no2)

    def Gun(self):      
        print(self.no1)
        print(self.no2)

def main():
    print("Enter first number :")
    a = int(input())

    print("Enter second number :")
    b = int(input())

    print("obj1 :")
    obj1 = Demo(a,b)
    obj1.Fun()
    obj1.Gun()

    print("Enter first number :")
    c = int(input())

    print("Enter second number :")
    d = int(input())

    print("obj2 :")
    obj2 = Demo(c,d)

    
    obj2.Fun()

    
    obj2.Gun()

if __name__ == "__main__":
    main()