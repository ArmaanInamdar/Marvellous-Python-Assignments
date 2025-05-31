import threading

def DisplayEven():
    print("Even Numbers :")
    for i in range(1,21):
        if(i % 2 == 0):
            print(i,end = ' ')
    print()

def DisplayOdd():
    print("Odd Numbers :")
    for i in range(1,20):
        if(i % 2 != 0):
            print(i,end = ' ')

def main():
    even = threading.Thread(target = DisplayEven)

    odd = threading.Thread(target = DisplayOdd)

    even.start()
    odd.start()
    even.join()
    odd.join()

if __name__ == "__main__":
    main()