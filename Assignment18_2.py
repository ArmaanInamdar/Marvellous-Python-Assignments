import os

def main():
    print("Enter the filename :")
    name = input()

    ret = os.path.exists(name)
    if(ret == True):
        fobj = open(name,'r')
        data = fobj.read()
        print(data)
    else:
        print("File does not exists")

if __name__ == "__main__":
    main()