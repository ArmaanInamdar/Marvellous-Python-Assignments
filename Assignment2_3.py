def Fact(no):
    ans1 = 1
    for i in range(1,no+1):
        ans1 = ans1 * i
    return ans1

def main():
    print("Enter number :")
    value1 = int(input())

    result = Fact(value1)
    print("Factorial is :",result)

if __name__ == "__main__":
    main()