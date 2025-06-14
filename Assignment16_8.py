
def main():
    fobj = open("data.txt",'r')
    data = fobj.readlines()
    fobj1 = open("clean.txt",'w')

    for i in data:
        if(i.strip()):
            fobj1.write(i)
            
    

if __name__ == "__main__":
    main()