import psutil

def processdisplay(name):
    
    for proc in psutil.process_iter():
        n1 = proc.name()
        if(n1 == name):
            info = proc.as_dict(attrs=['pid','name'])
            user = proc.username()
            print(info,end = ' ')
            print("user : "+user)

def main():
    print("Enter name of process :")
    name = input()
    processdisplay(name)

if __name__ == "__main__":
    main()