def Display(no):
    for i in range(1,no+1):
        for j in range(1,no+1):
            print(j,"\t",end = ' ')
        print("\n")
            
def main():
    print("Enter number :")
    value1 = int(input())

    Display(value1)

if __name__ == "__main__":
    main()