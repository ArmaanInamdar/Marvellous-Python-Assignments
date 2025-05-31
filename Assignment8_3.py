import threading

def DisplayEvenFactor(value):
    sum1 = 0
    for i in value:
        if(i % 2 == 0):
            sum1 = sum1 + i
    print("even sum :",sum1)

def DisplayOddFactor(value):
    sum2 = 0
    for i in value:
        if(i % 2 != 0):
            sum2 = sum2 + i
    print("odd sum :",sum2)

def main():
    print("Enter number of element yo want :")
    no1 = int(input())
    L1 = []
    print("Enter elements :")
    for i in range(no1):
        no2 = int(input())
        L1.append(no2)

    evenlist = threading.Thread(target = DisplayEvenFactor,args = (L1,))

    oddlist = threading.Thread(target = DisplayOddFactor,args = (L1,))

    evenlist.start()
    oddlist.start()
    evenlist.join()
    oddlist.join()

    
    

if __name__ == "__main__":
    main()