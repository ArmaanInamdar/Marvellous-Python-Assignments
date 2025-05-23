def SumEven():
    sum = 0
    for i in range(1,101):
        if(i % 2 == 0):
            sum = sum + i
    return sum

def main():

    result = SumEven()

    print("Sum of even numbers between 1 to 100 is :",result)

if __name__ == "__main__":
    main()