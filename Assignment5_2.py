def ChkVowel(A):
    V = ['A','E','I','O','U','a','e','i','o','u']
    for i in V:
        if(A == i):
            return True
    return False

def main():
    print("Enter letter :")
    str1 = input()

    result = ChkVowel(str1)

    if(result == True):
        print("It is Vowel")
    else:
        print("It is consonant")

if __name__ == "__main__":
    main()