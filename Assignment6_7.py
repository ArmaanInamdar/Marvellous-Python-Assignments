def Largest(A):
    B = 0
    for i in range(len(A)):
        if(A[i] > B):
            B = A[i]
    return B

def main():
    Data = []
    print("Enter numbers :")
    for i in range(0,5):
        no1 = int(input())
        Data.append(no1)

    result = Largest(Data)

    print("Maximum number is :",result)

if __name__ == "__main__":
    main()