import multiprocessing

def Square(no):
    List1 = []
    for i in no:
        i = i**2
        List1.append(i)
    print(List1)

def main():
    L1 = [1,2,3,4,5]
    L2 = [3,2,5,3,2]
    p1 = multiprocessing.Process(target = Square,args = (L1,))
    p2 = multiprocessing.Process(target = Square,args = (L2,))
    
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    

if __name__ == "__main__":
    main()