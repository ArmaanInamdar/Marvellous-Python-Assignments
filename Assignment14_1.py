class Employee:

    def __init__(self,A,B,C):
        self.name = A   
        self.emp_id = B 
        self.salary = C         

    def Display(self):
        print(self.name)
        print("ID :",self.emp_id)
        print("salary :",self.salary)


def main():
    obj1 = Employee("Rohit",101,50000)
    obj2 = Employee("Yogesh",102,15000)
    obj1.Display()
    obj2.Display()
    

if __name__ == "__main__":
    main()