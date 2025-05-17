def Addition(no1):
    sum = 0
    for i in range(len(no1)):
        sum = sum + no1[i]
    return sum

def main():
    print("Enter the number of elements :")
    no = int(input())

    data = []
    print("Enter elements :")
    for i in range(no):
        value = int(input())
        data.append(value)

    result = Addition(data)

    print("Addition is :",result)

if __name__ == "__main__":
    main()