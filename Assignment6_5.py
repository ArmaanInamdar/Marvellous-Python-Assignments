def Prime(no):
    for i in range(2,no):
        if(no % i == 0):
            return False
        return True

def main():

    print("Enter number :")
    no1 = int(input())

    result = Prime(no1)

    if(result == True):
        print(no1,"is a Prime number")
    else:
        print(no1,"is not a Prime number")

if __name__ == "__main__":
    main()