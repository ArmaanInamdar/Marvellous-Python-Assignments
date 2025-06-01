p = 0

def power(A,B):
    global p
    while(p == 0):
        p = A**B
        power(A,B)
    return p

def main():
    print('Enter number :')
    no1 = int(input())
    no2 = int(input())
    ret = power(no1,no2)
    print(ret)

if __name__ == "__main__":
    main()