
def ChkNum(no1):
    if((no1 % 2) == 0):
        return True
    else:
        return False

def main():
    print("Enter number :")
    value1 = int(input())

    result = ChkNum(value1)

    if(result == True):
        print("Number is Even")
    else:
        print("Number is Odd")


if __name__ == "__main__":
    main()