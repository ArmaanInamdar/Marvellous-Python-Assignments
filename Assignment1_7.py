
def ChkDivisible(no1):
    if ((no1 % 5) == 0):
        return True
    else:
        return False

def main():
    print("Enter number :")
    value1 = int(input())

    result = ChkDivisible(value1)

    if(result == True):
        print(result)
    else:
        print(result)


if __name__ == "__main__":
    main()