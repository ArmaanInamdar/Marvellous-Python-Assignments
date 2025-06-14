import os

def main():
    print("Enter first file name :")
    filename1 = input()

    print("Enter string :")
    str = input()
    count = 0

    ret1 = os.path.exists(filename1)

    if(ret1 == True):
        fobj1 = open(filename1,'r')
        data1 = fobj1.read()
        data = data1.split()
        for i in data:
            if(i == str):
                count = count + 1
        print(count)
    else:
        print("one of the two files is not present")


if __name__ == "__main__":
    main()