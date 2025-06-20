import psutil
import os

def processdisplay(name):
    ret = os.path.isabs(name)
    if(ret == False):
        name = os.path.abspath(name)

    filename = os.path.join(name,"log.txt")
    
    fobj = open(filename,'w')

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid','name'])
        user = proc.username()
        fobj.write(str(info))
        fobj.write("user : "+user)
        fobj.write("\n")

def main():
    print("Enter directory name :")
    name = input()
    processdisplay(name)

if __name__ == "__main__":
    main()