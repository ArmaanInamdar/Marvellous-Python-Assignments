def Prime(no):
    for i in range(2,no):
        if(no % i == 0):
            return False
        return True

def main():
    print("Enter number :")
    value1 = int(input())

    result = Prime(value1)
    if(result == True):
        print("Number is Prime")
    else:
        print("Number is not Prime")


if __name__ == "__main__":
    main()