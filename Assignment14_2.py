class Rectangle:

    def __init__(self,A,B):
        self.length = A   
        self.width = B 
                
    def Area(self): 
        return self.length * self.width

    def Perimeter(self):
        return (self.length + self.width) * 2


def main():
    obj1 = Rectangle(12,6)
    obj2 = Rectangle(10,5)
    print("Area :",obj1.Area())
    print("Perimeter :",obj1.Perimeter())
    print("Area :",obj2.Area())
    print("Perimeter :",obj2.Perimeter())
    

if __name__ == "__main__":
    main()