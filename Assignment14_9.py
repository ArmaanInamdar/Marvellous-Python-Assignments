class Product:

    def __init__(self,A,B):
        self.name = A
        self.price = B

    def __eq__(self,C):
        return self.price == C.price

    
def main():
    p1 = Product("Book",100)
    p2 = Product("Pen",100)
    p3 = Product("Bag",300)

    print(p1 == p2)
    print(p1 == p3)
    

if __name__ == "__main__":
    main()