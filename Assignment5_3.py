def Voting(A):
    if(A >= 18):
        return True
    else:
        return False

def main():
    print("Enter age :")
    no1 = int(input())

    result = Voting(no1)

    if(result == True):
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")

if __name__ == "__main__":
    main()