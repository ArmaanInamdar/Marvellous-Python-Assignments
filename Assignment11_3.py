Sum = 0

def Add(no):
    global Sum
    if(no >= 1):
        digit = no % 10
        Sum = Sum + digit
        no = no / 10
        Add(no)
    return Sum

def main():
    print('Enter number :')
    no1 = int(input())
    ret = int(Add(no1))
    print(ret)

if __name__ == "__main__":
    main()