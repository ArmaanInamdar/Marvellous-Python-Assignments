from functools import Product

def filterX(Task,value):
    no = Task(value)
    return no


def main():
    print("Enter the number of elements to insert :")
    no = int(input())
    Data = []
    print("Enter numbers :")
    for i in range(0,no):
        no1 = int(input())
        Data.append(no1)

    result = filterX(Product,Data)

    print(result)

if __name__ == "__main__":
    main()