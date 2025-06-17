import os
import sys
import time
import shutil
import schedule

def DirectoryWatcher(DirectoryName1,DirectoryName2,Extention):
    
    Flag = os.path.isabs(DirectoryName1)
    if(Flag == False):
        DirectoryName1 = os.path.abspath(DirectoryName1)

    flag = os.path.exists(DirectoryName1)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName1)

    if(flag == False):
        print("The path is valid but the target is not directory")
        exit()

    flag = os.path.exists(DirectoryName2)
    if(flag == False):
        os.mkdir(DirectoryName2)
    else:
        print("Directory is already present")
    
    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName1):
        F1 = []
        for fname in FileNames:
            if(fname.endswith(Extention)):
                F1.append(fname)
                fname = os.path.join(FolderName,fname)
                shutil.copy(fname,DirectoryName2)
            
                

    timestamp = time.ctime()
    
    FileName = "MarvellousLog %s.log" %(timestamp)
    FileName = FileName.replace(" ","_")
    FileName = FileName.replace(":","_")

    fobj = open(FileName,"w")

    print("Files copied to destination folder !!!")
    print("Record written in "+FileName)


    Border = "-"*70
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write(Border+"\n")

    for i in F1:
        fobj.write(i+" copied to "+DirectoryName2+" Folder")
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

    elif(len(sys.argv) == 4):
        DirectoryWatcher(sys.argv[1],sys.argv[2],sys.argv[3])

    else:
        print("Invalid number of command line arguments")
        print("Use the given Flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")


if __name__ == "__main__":
    main()