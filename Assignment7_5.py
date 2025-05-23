def palindrome(A):
    Data1 = []
    Data2 = []
    for i in A:
        Data1.append(i)
    for i in reversed(A):
        Data2.append(i)
    
    if(Data1 == Data2):
        return True
    else:
        return False
    

def main():
    print("Enter string :")
    str = input()
    
    result = palindrome(str)

    if(result == True):
        print("It is palindrome")
    else:
        print("It is not palindrome")

if __name__ == "__main__":
    main()