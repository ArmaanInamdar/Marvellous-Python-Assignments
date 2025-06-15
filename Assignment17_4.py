import schedule
import time
import datetime

def Display():
    print("Namskar")
    print()

def main():

    schedule.every(30).day.at("9:00").do(Display)

    print("Application running :")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()