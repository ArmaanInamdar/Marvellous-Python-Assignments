def Fact(no):
    A = 1
    for i in range(1,no+1):
        A = A * i
    return A

def main():

    print("Enter number :")
    no1 = int(input())

    result = Fact(no1)

    print("Factorial of ",no1,"is :",result)

if __name__ == "__main__":
    main()