def Mul(no):
    A = 1
    for i in range(1,11):
        A = no * i
        print(no," X ",i, " = ",A)

def main():

    print("Enter number :")
    no1 = int(input())

    Mul(no1)

if __name__ == "__main__":
    main()