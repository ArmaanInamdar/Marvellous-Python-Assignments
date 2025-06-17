import os

def main():
    print("Enter the filename :")
    name1 = input()
    print("Enter string :")
    str1 = input()
    count = 0

    ret = os.path.exists(name1)
    if(ret == True):
        fobj = open(name1,'r')
        data = fobj.read()
        data = data.split(" ")
        for i in data:
            if(i == str1):
                count = count + 1
        print("Frequency is :",count)
    else:
        print("File does not exists")

if __name__ == "__main__":
    main()
    

