import threading

def DisplayEvenFactor(value):
    sum1 = 0
    for i in range(1,value+1):
        if((value % i == 0) and (i % 2 == 0)):
            sum1 = sum1 + i
    print("even factor sum :",sum1)

def DisplayOddFactor(value):
    sum2 = 0
    for i in range(1,value+1):
        if((value % i == 0) and (i % 2 != 0)):
            sum2 = sum2 + i
    print("odd factors sum :",sum2)

def main():
    print("Enter number :")
    no = int(input())

    evenfactor = threading.Thread(target = DisplayEvenFactor,args = (no,))

    oddfactor = threading.Thread(target = DisplayOddFactor,args = (no,))

    evenfactor.start()
    oddfactor.start()
    evenfactor.join()
    oddfactor.join()

    print("exit from main")
    

if __name__ == "__main__":
    main()