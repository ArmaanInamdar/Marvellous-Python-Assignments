import schedule
import time

def Display():
    print("Jay Ganesh")
    print()

def main():

    schedule.every(2).seconds.do(Display)

    print("Application running :")

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()