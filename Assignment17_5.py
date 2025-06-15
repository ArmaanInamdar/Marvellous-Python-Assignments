import schedule
import time
import datetime

def job():
    fobj = open("Marvellous.txt",'a')
    fobj.write(str(datetime.datetime.now()))
    fobj.write("\n")

def main():

    schedule.every(5).minutes.do(job)

    print("Application running :")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()