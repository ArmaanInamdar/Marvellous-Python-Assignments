import threading
import time

def Display1():
    for i in range(1,6):
        print(i)

def Display2():
    for i in range(1,6):
        print(i)

def Display3():
    for i in range(1,6):
        print(i)

def main():
    T1 = threading.Thread(target = Display1)
    T2 = threading.Thread(target = Display2)
    T3 = threading.Thread(target = Display3)

    T1.start()
    T1.join()
    time.sleep(1)

    T2.start()
    T2.join()
    time.sleep(1)

    T3.start()
    T3.join()
    

if __name__ == "__main__":
    main()