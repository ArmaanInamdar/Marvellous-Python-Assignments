def Sum(A,B):
    return A + B

def Difference(A,B):
    if(A > B):
        return A - B
    else:
        return B - A

def Product(A,B):
    return A * B

def Division(A,B):
    return A / B

def main():
    print("Enter first number :")
    no1 = int(input())

    print("Enter second number :")
    no2 = int(input())

    ans1 = Sum(no1,no2)
    ans2 = Difference(no1,no2)
    ans3 = Product(no1,no2)
    ans4 = Division(no1,no2)

    print("Sum is :",ans1)
    print("Difference is :",ans2)
    print("Product is :",ans3)
    print("Division is :",ans4)   

if __name__ == "__main__":
    main()