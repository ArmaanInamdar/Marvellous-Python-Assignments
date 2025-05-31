import multiprocessing
import threading
import time

def Sum1(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + i
    return sum

def Sum2(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + i
    print(sum)

def main():
    data = 10000000
    
    start_time = time.time()
    result = Sum1(data)
    print(result)
    end_time = time.time()
    print("Time taken in normal function is :",end_time-start_time)


    t1 = threading.Thread(target = Sum2,args = (data,))
    p1 = multiprocessing.Process(target = Sum2,args = (data,))

    start_time = time.time()
    t1.start()
    t1.join()
    end_time = time.time()
    print("Time taken in thread is :",end_time-start_time)

    start_time = time.time()
    p1.start()
    p1.join()
    end_time = time.time()
    print("Time taken in multiprocessing is :",end_time-start_time)

if __name__ == "__main__":
    main()