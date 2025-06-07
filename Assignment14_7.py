class Person:
    school_name = "\0"

    def __init__(self,A,B):
        self.name = A   
        self.age = B 

class Teacher(Person):
    def __init__(self,C,D,A,B):
        super().__init__(A,B)
        self.subject = C   
        self.salary = D 
    
    def Display(self):
        print("Name:"+ self.name)
        print("Age:", self.age)
        print("Subject:"+ self.subject)
        print("Salary:", self.salary)

def main():
    obj2 = Teacher("English", 15000, "Rohit", 30)
    obj2.Display()
    

if __name__ == "__main__":
    main()