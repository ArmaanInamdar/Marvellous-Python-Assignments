i = 1

def Display(no):
    global i
    if(no >= 1):
        print(i)
        i = i + 1
        no = no -1
        Display(no)

def main():
    print('Enter number :')
    no1 = int(input())
    Display(no1)

if __name__ == "__main__":
    main()