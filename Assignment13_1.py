class BookStore:
    NoofBooks = 0

    def __init__(self,A,B):   
        self.Name = A          
        self.Author = B

    def Display(self):
        BookStore.NoofBooks =  BookStore.NoofBooks + 1     
        print("Name :"+self.Name)
        print("Author :"+self.Author)
        print("Number of Books :",BookStore.NoofBooks)


def main():
    print("Enter name and author :")
    name = input()
    author = input()
    obj1 = BookStore(name,author)
    print("Enter name and author :")
    name = input()
    author = input()
    obj2 = BookStore(name,author)

    obj1.Display()
    obj2.Display()
    
    

if __name__ == "__main__":
    main()