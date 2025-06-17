import os

def main():
    print("Enter the filename :")
    name1 = input()
    print("Enter the filename :")
    name2 = input()

    ret = os.path.exists(name1,name2)
    if(ret == True):
        fobj = open(name,'r')
        fobj2 = open("Demo.txt",'w')
        data = fobj.read()
        fobj2.write(data)
    else:
        print("File does not exists")

if __name__ == "__main__":
    main()
    

