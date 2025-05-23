def Display():
    for i in range(1,5):
        for j in range(1,5):
            if(i > j or i == j):
                print("*\t",end = ' ')
            else:
                print(" ",end = ' ')
        print("\n")
            
def main():

    Display()

if __name__ == "__main__":
    main()