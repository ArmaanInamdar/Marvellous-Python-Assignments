import os

def main():
    print("Enter the filename :")
    name = input()

    ret = os.path.exists(name)

    if(ret == True):
        print(name+" exists")
    else:
        print(name+" does not exists")

if __name__ == "__main__":
    main()