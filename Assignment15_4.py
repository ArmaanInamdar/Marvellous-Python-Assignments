import os

def main():
    print("Enter first file name :")
    filename1 = input()

    print("Enter second file name :")
    filename2 = input()

    ret1 = os.path.exists(filename1)
    ret2 = os.path.exists(filename2)

    if((ret1 == True) and (ret2 == True)):
        fobj1 = open(filename1,'r')
        data1 = fobj1.read()
        fobj2 = open(filename2,'r')
        data2 = fobj2.read()
        if(data1 == data2):
            print("Contents of "+filename1+ " and "+filename2+" is same")
        else:
            print("Content is not same")
    else:
        print("one of the two files is not present")


if __name__ == "__main__":
    main()