Square = lambda A : A**2

Cube = lambda A : A**3

def main():

    print("Enter number :")
    no1 = int(input())

    result1 = Square(no1)

    result2 = Cube(no1)

    print("Square :",result1)
    print("Cube :",result2)


if __name__ == "__main__":
    main()