def Maximum(no1):
    Max = 0
    for i in range(len(no1)):
        if(no1[i] > Max):
            Max = no1[i]
    return Max

def main():
    print("Enter the number of elements :")
    no = int(input())

    data = []
    print("Enter elements :")
    for i in range(no):
        value = int(input())
        data.append(value)

    result = Maximum(data)

    print("Maximum number is :",result)

if __name__ == "__main__":
    main()