import psutil

def processdisplay():
    
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','name'])
        user = proc.username()
        print(info,end = ' ')
        print("user : "+user)

def main():
    processdisplay()

if __name__ == "__main__":
    main()