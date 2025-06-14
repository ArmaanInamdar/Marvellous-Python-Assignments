
def main():
    fobj = open("Assignment16_1.py",'r')
    data = fobj.read()
    ccount = 0
    wcount = 0

    for i in data:
        if(i != " "):
            ccount = ccount + 1
    
    data = data.split()
    for i in data:
        if(i != " "):
            wcount = wcount + 1

    fobj1 = open("Assignment16_1.py",'r')
    lines = fobj1.readlines()
    lcount = len(lines)

    print("number of characters are :",ccount)
    print("number of words are :",wcount)
    print("number of lines are :",lcount)




    print(data)

if __name__ == "__main__":
    main()