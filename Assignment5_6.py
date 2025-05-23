def Fahren(A):
    F = (A * 9/5) + 32
    return F

def main():
    print("Enter temperature in Celsius :")
    no1 = int(input())

    result = Fahren(no1)

    print("Temperature in Fahrenheit :",result)

if __name__ == "__main__":
    main()