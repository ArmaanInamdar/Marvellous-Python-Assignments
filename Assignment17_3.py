import schedule
import time
import datetime

def Display():
    print("Do Coding....!")
    print()

def main():

    schedule.every(30).minutes.do(Display)

    print("Application running :")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()