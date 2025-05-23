Even = lambda A : (A % 2 == 0)

def filterX(Task,value):
    Result = []
    for i in range(len(value)):
        no = Task(value[i])
        if(no == True):
            Result.append(value[i])
    return Result


def main():
    print("Enter the number of elements to insert :")
    no = int(input())
    Data = []
    print("Enter numbers :")
    for i in range(0,no):
        no1 = int(input())
        Data.append(no1)

    result = filterX(Even,Data)

    print(result)

if __name__ == "__main__":
    main()