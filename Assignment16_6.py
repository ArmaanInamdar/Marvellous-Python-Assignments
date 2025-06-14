
def main():
    fobj = open("data.txt",'r')
    data = fobj.read()

    fobj1 = open("Hello.txt",'w')
    fobj1.write(data)

if __name__ == "__main__":
    main()