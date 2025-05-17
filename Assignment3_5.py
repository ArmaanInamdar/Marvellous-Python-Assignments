from MarvellousNum import ChkPrime

def ListPrime(no1):
    Result = []
    sum = 0
    for i in range(len(no1)):
        value = ChkPrime(no1[i])
        if(value == True):
            Result.append(no1[i])

    for i in range(len(Result)):
        sum = sum + Result[i]

    return sum


def main():
    print("Enter the number of elements :")
    no = int(input())

    data = []
    print("Enter elements :")
    for i in range(no):
        value = int(input())
        data.append(value)

    result = ListPrime(data)

    print("Addition of prime numbers is :",result)

if __name__ == "__main__":
    main()