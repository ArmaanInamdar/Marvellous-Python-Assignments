def Count(no):
    count = 0
    while(no != 0):
        no = int((no / 10))
        count = count + 1
    return count

def main():
    print("Enter number :")
    value1 = int(input())

    result = Count(value1)
    
    print(int(result))


if __name__ == "__main__":
    main()