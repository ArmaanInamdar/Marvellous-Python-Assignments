class Student:
    school_name = "\0"

    def __init__(self,A,B):
        self.name = A   
        self.roll_no = B 

    def Display(self,A): 
        print("name :"+self.name)
        print("roll no :",self.roll_no)
        Student.school_name = A
        print("School :"+Student.school_name)

def main():
    obj1 = Student("Rahul",10)
    obj2 = Student("Mohit",12)
    obj1.Display("Marvellous")
    obj2.Display("Unique")
    

if __name__ == "__main__":
    main()