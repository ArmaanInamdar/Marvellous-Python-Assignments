import os
import sys
import time
import hashlib

def DirectoryWatcher(DirectoryName):
    
    Flag = os.path.isabs(DirectoryName)
    if(Flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("The path is valid but the target is not directory")
        exit()

    
    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        F1 = []
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            fobj = open(fname,'rb')

            hobj = hashlib.md5()

            buffer = fobj.read(1024)
            while(len(buffer) > 0):
                hobj.update(buffer)
                buffer = fobj.read(1024)

            fobj.close()

            print("Checksum of "+fname+" is :",hobj.hexdigest())
            

def main():

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the Automation Script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given Script as :")
            print("ScriptName.py NameofDirectory Expected_Extention")
            print("Please provide valid absolut path")

        elif(len(sys.argv) == 2):
            DirectoryWatcher(sys.argv[1])

    else:
        print("Invalid number of command line arguments")
        print("Use the given Flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")


if __name__ == "__main__":
    main()