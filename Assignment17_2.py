import schedule
import time
import datetime

def Display():
    print("Inside MySchedule function at :",datetime.datetime.now())
    print()

def main():

    schedule.every(1).minutes.do(Display)

    print("Application running :")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()