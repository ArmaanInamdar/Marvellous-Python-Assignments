Product = lambda A,B : A*B
ChkNum = lambda A : (A >= 70 and A <= 90)
Increase = lambda A : A + 10


def filterX(Task,Values):
    Result = []
    for no in Values:
        Ret = Task(no)
        if(Ret == True):
            Result.append(no)

    return Result

def mapX(Task,Values):
    Result = []
    for no in Values:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def reduceX(Task,Values):
    Result = 1
    for no in Values:
        Result = Task(Result,no)

    return Result

def main():
    Data = []
    print("Enter number of elements :")
    size = int(input())

    print("Enter Data :")

    for i in range(size):
        no = int(input())
        Data.append(no)

    FData = list(filterX(ChkNum,Data))
    print("Filter Output :",FData)

    MData = list(mapX(Increase,FData))
    print("Map Output :",MData)

    RData = int(reduceX(Product,MData))
    print("Reduce Output :",RData)

if __name__ == "__main__":
    main()