
def Add(no1,no2):
    ans = no1 + no2
    return ans

def main():
    print("Enter first number :")
    value1 = int(input())

    print("Enter second number :")
    value2 = int(input())

    result = Add(value1,value2)

    print("Addition is :",result)

if __name__ == "__main__":
    main()