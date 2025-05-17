def AddDigit(no):
    sum = 0
    while(no != 0):
        i = no % 10
        sum = sum + i 
        no = int((no / 10))
    return sum

def main():
    print("Enter number :")
    value1 = int(input())

    result = AddDigit(value1)
    
    print(int(result))


if __name__ == "__main__":
    main()