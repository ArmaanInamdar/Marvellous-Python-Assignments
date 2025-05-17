def Display(no):
    for i in range(no):
        for j in range(no):
            print("*\t",end = ' ')
        print("\n")
            
def main():
    print("Enter number :")
    value1 = int(input())

    Display(value1)

if __name__ == "__main__":
    main()