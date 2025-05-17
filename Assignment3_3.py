def Minimum(no1):
    Min = no1[0]
    for i in range(len(no1)):
        if(no1[i] < Min):
            Min = no1[i]
    return Min

def main():
    print("Enter the number of elements :")
    no = int(input())

    data = []
    print("Enter elements :")
    for i in range(no):
        value = int(input())
        data.append(value)

    result = Minimum(data)

    print("Minimum number is :",result)

if __name__ == "__main__":
    main()