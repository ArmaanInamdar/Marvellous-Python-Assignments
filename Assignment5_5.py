def ChkEvenOdd(A):
    if(A % 2 == 0):
        return True
    else:
        return False

def main():
    print("Enter number :")
    no1 = int(input())

    result = ChkEvenOdd(no1)

    if(result == True):
        print("It is even number")
    else:
        print("It is odd number")

if __name__ == "__main__":
    main()