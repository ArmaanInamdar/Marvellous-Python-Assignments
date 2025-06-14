
def main():
    numbers = []
    print("Enter numbers :")

    for i in range(10):
        no = int(input())
        numbers.append(no)
    
    fobj = open("numbers.txt",'a')
    for i in numbers:
        fobj.write(str(i))
        fobj.write("\n")


if __name__ == "__main__":
    main()