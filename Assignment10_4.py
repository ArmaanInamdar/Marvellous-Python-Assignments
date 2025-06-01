Square = lambda A : A**2
ChkEven = lambda A : (A % 2 == 0)
add = lambda A,B : A + B


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
    Result = 0
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

    FData = list(filterX(ChkEven,Data))
    print("Filter Output :",FData)

    MData = list(mapX(Square,FData))
    print("Map Output :",MData)

    RData = int(reduceX(add,MData))
    print("Reduce Output :",RData)

if __name__ == "__main__":
    main()