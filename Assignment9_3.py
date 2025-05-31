import multiprocessing

def Factorial(no):
    sum = 1
    for i in range(1,no+1):
        sum = sum * i
    return sum

def main():
    data = [22,12,4,15,21]
    Result = []

    
    p = multiprocessing.Pool()
    Result = p.map(Factorial,data)

    p.close()
    p.join()

    print(Result)

if __name__ == "__main__":
    main()