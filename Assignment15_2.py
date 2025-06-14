import os

def main():
    print("Enter file name :")
    filename = input()

    ret = os.path.exists(filename)

    if(ret == True):
        fobj = open(filename,'r')
        data = fobj.read()
        print(data)
    else:
        print(filename+" is not present")


if __name__ == "__main__":
    main()