import os

def main():
    print("Enter the filename :")
    name1 = input()
    print("Enter the filename :")
    name2 = input()

    ret1 = os.path.exists(name1)
    ret2 = os.path.exists(name2)
    if((ret1 == True) and (ret2 == True)):
        fobj = open(name1,'r')
        fobj2 = open(name2,'r')
        data1 = fobj.read()
        data2 = fobj2.read()
        if(data1 == data2):
            print("Content is same")
        else:
            print("Content is not same")
    else:
        print("File does not exists")

if __name__ == "__main__":
    main()
    

