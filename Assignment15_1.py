import os

def main():
    print("Enter file name :")
    filename = input()

    ret = os.path.exists(filename)

    if(ret == True):
        print(filename+" is present")
    else:
        print(filename+" is not present")

if __name__ == "__main__":
    main()