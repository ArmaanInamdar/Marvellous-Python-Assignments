
def main():
    fobj = open("marks.txt",'r')
    data = fobj.read()

    data = data.split()
    for i in range(len(data)):
        ret = data[i].isdigit()
        if(ret == True):
            marks = int(data[i])
            if(marks > 75):
                print(data[i-1],end = ' ')
                print(data[i])

if __name__ == "__main__":
    main()