import schedule
import time
import datetime

def backup():
    fobj = open("Marvellous.txt",'r')
    data = fobj.read()
    fobj1 = open("backup.txt",'a')
    fobj1.write(data)
    fobj1.write("\n")
    fobj2 = open("backup_log.txt",'a')
    fobj2.write("backup done at : "+str(datetime.datetime.now()))
    fobj2.write("\n")


def main():

    schedule.every(5).seconds.do(backup)

    print("Application running :")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()