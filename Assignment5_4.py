def LargestNum(A,B,C):
    if(A > B and A > C):
        return A
    elif(B > A and B > C):
        return B
    return C

def main():
    print("Enter first number :")
    no1 = int(input())

    print("Enter second number :")
    no2 = int(input())

    print("Enter third number :")
    no3 = int(input())

    result = LargestNum(no1,no2,no3)

    print("Largest number is :",result)

if __name__ == "__main__":
    main()