Sum = 0

def SumNat(no):
    global Sum
    if(no >= 1):
        Sum = Sum + no
        no = no -1
        SumNat(no)
    return Sum

def main():
    print('Enter number :')
    no1 = int(input())
    ret = SumNat(no1)
    print(ret)

if __name__ == "__main__":
    main()