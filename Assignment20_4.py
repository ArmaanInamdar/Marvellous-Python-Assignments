import os
import sys
import time
import hashlib
import datetime

def CalculateCheckSum(path, BlockSize = 1024):
    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):
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
    
    Duplicate = {}

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname) 
            checksum = CalculateCheckSum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate


def DeleteDuplicate(path):

    MyDict = FindDuplicate(path)
    D1 = []
    Result = list(filter(lambda x : len(x) > 1 , MyDict.values()))
    count = 0
    Cnt = 0
    for value in Result:
        for subvalue in value:
            count = count + 1
            if(count > 1):
                print("Deleted file :",subvalue)
                D1.append(subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1
        count = 0
    
    print("Total deleted file :",Cnt)
    return D1

def DisplayResult(L1,TT):
    

    timestamp = time.ctime()
    
    FileName = "log.txt"

    fobj = open(FileName,"w")

    print("Record written in "+FileName+" with time taken")


    Border = "-"*70
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write(Border+"\n")

    for i in L1:
        fobj.write(i+" Deleted")
        fobj.write("\n")
    
    fobj.write("Time taken to execute :"+str(TT))

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
            print("ScriptName.py NameofDirectory")
            print("Please provide valid absolut path")

        else:
            starttime = time.time()
            ret = DeleteDuplicate(sys.argv[1])
            endtime = time.time()
            timetaken = endtime - starttime
            DisplayResult(ret,timetaken)
            
    else:
        print("Invalid number of command line arguments")
        print("Use the given Flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()