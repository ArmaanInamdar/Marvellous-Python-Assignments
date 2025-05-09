
def ChkNegPos(no1):
    if no1 < 0:
        return True
    else:
        return False

def main():
    print("Enter number :")
    value1 = int(input())

    result = ChkNegPos(value1)

    if(result == True):
        print("Number is Negative")
    else:
        print("Number is Positive")


if __name__ == "__main__":
    main()