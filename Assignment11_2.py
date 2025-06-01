Fact = 1

def Factorial(no):
    global Fact
    if(no >= 1):
        Fact = Fact * no
        no = no -1
        Factorial(no)
    return Fact

def main():
    print('Enter number :')
    no1 = int(input())
    ret = Factorial(no1)
    print(ret)

if __name__ == "__main__":
    main()