import threading

def ChkSmall(str2):
    L1 = 0
    for i in str2:
        if((ord(i) >= 97) and (ord(i) <= 122)):
            L1 = L1 + 1
    print("Thread ID of small is :",threading.get_ident())
    print("Number of Small :",L1)

def ChkCapital(str2):
    L2 = 0
    for i in str2:
        if((ord(i) >= 65) and (ord(i) <= 90)):
            L2 = L2 + 1
    print("Thread ID of Capital is :",threading.get_ident())
    print("Number of Capital :",L2)

def ChkDigits(str2):
    L3 = 0
    for i in str2:
        if((ord(i) >= 48) and (ord(i) <= 57)):
            L3 = L3 + 1
    print("Thread ID of Digits is :",threading.get_ident())
    print("Number of Digits :",L3)
    
def main():
    print("Enter string")
    str1 = input()

    small = threading.Thread(target = ChkSmall,args = (str1,))
    capital = threading.Thread(target = ChkCapital,args = (str1,))
    digits = threading.Thread(target = ChkDigits,args = (str1,))

    small.start()
    capital.start()
    digits.start()
    small.join()
    capital.join()
    digits.join()
    

if __name__ == "__main__":
    main()