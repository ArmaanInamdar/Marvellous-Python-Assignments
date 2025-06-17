import os
import sys
import time

def DirectoryWatcher(DirectoryName,Extention):
    
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
            if(fname.endswith(Extention)):
                print(fname)
                F1.append(fname)

    timestamp = time.ctime()
    
    FileName = "MarvellousLog %s.log" %(timestamp)
    FileName = FileName.replace(" ","_")
    FileName = FileName.replace(":","_")

    fobj = open(FileName,"w")

    Border = "-"*70
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write(Border+"\n")

    for i in F1:
        fobj.write(i)
        fobj.write("\n")
    

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("This file is created at :\n"+timestamp+"\n")
    fobj.write(Border+"\n")

                

def main():

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the Automation Script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given Script as :")
            print("ScriptName.py NameofDirectory Expected_Extention")
            print("Please provide valid absolut path")

    elif(len(sys.argv) == 3):
        DirectoryWatcher(sys.argv[1],sys.argv[2])

    else:
        print("Invalid number of command line arguments")
        print("Use the given Flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")


if __name__ == "__main__":
    main()