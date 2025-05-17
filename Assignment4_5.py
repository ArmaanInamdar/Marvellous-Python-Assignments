def Max(A):
    B = 1
    if(A > B):
        B = A
    return B

def Prime(A):
    for i in range(2,A):
        if(A % i == 0):
            return False
    return True

def Mul(A):
    A = A * 2
    return A


def filterX(Values):
    Result = []
    for no in Values:
        Ret = Prime(no)
        if(Ret == True):
            Result.append(no)

    return Result

def mapX(Values):
    Result = []
    for no in Values:
        Ret = Mul(no)
        Result.append(Ret)

    return Result

def reduceX(Values):
    Result = 0
    for no in Values:
        Result = Max(no)

    return Result

def main():
    Data = []
    print("Enter number of elements :")
    size = int(input())

    print("Enter Data :")

    for i in range(size):
        no = int(input())
        Data.append(no)

    FData = list(filterX(Data))
    print("Filter Output :",FData)

    MData = list(mapX(FData))
    print("Map Output :",MData)

    RData = int(reduceX(MData))
    print("Reduce Output :",RData)

if __name__ == "__main__":
    main()