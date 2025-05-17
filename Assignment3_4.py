def Frequency(no1,no2):
    Freq = 0
    for i in range(len(no1)):
        if(no1[i] == no2):
            Freq = Freq + 1
    return Freq

def main():
    print("Enter the number of elements :")
    no = int(input())

    data = []
    print("Enter elements :")
    for i in range(no):
        value = int(input())
        data.append(value)

    print("Element search :")
    value1 = int(input())

    result = Frequency(data,value1)

    print("Frequency is :",result)

if __name__ == "__main__":
    main()