count = 0

def count_zeros(no):
    global count
    if(no >= 1):
        digit = no % 10
        if(digit == 0):
            count = count + 1
        no = no / 10
        no = int(no)
        count_zeros(no)
    return count

def main():
    print('Enter number :')
    no1 = int(input())
    ret = int(count_zeros(no1))
    print(ret)

if __name__ == "__main__":
    main()