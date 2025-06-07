class Employee:

    def __init__(self,A,B,C):
        self.name = A   
        self._department = B 
        self.__salary = C         

    def Display(self):
        print("name :",self.name)
        print("department :",self._department)


def main():
    obj1 = Employee("Rohit","Hr",50000)
    obj2 = Employee("Yogesh","voice",15000)
    obj1.Display()
    obj2.Display()
    

if __name__ == "__main__":
    main()