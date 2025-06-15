import schedule
import time
import datetime

def job1():
    print("Lunch Time")

def job2():
    print("Wrap up work")

def main():

    schedule.every().day.at("13:00").do(job1)
    schedule.every().day.at("18:00").do(job2)

    print("Application running :")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()