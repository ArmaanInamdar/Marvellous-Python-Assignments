class Book:

    def __init__(self):
        self.__price = 0 
                
    def get(self): 
        print("Enter price :")
        self.no = int(input())

    def set(self):
        self.__price = self.no
        print("price set")


def main():
    obj1 = Book()
    obj1.get()
    obj1.set()
    

if __name__ == "__main__":
    main()