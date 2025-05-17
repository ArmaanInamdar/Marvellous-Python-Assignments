def AddFact(no):
    ans = 0
    for i in range(1,no):
        if(no % i == 0):
            ans = ans + i
    return ans

def main():
    print("Enter number :")
    value1 = int(input())

    result = AddFact(value1)
    
    print("Result is :",result)


if __name__ == "__main__":
    main()