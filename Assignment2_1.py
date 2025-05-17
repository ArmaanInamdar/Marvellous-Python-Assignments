from Arithmetic import Add,Sub,Mul,Div

def main():
    print("Enter 1 if Addition")
    print("Enter 2 if Substraction")
    print("Enter 3 if Multiplication")
    print("Enter 4 if Division")
    value1 = int(input())

    print("Enter first number :")
    value2 = int(input())
    print("Enter second number:")
    value3 = int(input())

    if(value1 == 1):
        result = Add(value2,value3)
    elif(value1 == 2):
        result = Sub(value2,value3)
    elif(value1 == 3):
        result = Mul(value2,value3)
    elif(value1 == 4):
        result = Div(value2,value3)

    print("Result is :",result)

if __name__ == "__main__":
    main()