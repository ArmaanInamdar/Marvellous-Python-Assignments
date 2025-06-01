i = 0 
j = 0

def Display(no):
    global i
    global j
    if(i <= no):
        if(j <= i):
            print("*", "\t", end=' ')
            j = j + 1
            Display(no)
        else:
            print("\n")
            i = i + 1
            j = 1
            Display(no)
    

def main():
    print('Enter number :')
    no1 = int(input())
    Display(no1)

if __name__ == "__main__":
    main()

