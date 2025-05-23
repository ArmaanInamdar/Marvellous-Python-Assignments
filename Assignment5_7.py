def Area(L,W):
    ans = L * W
    return ans

def Peri(L,W):
    ans = (L + W) * 2
    return ans


def main():
    print("Enter Length :")
    no1 = int(input())

    print("Enter Width:")
    no2 = int(input())

    result1 = Area(no1,no2)

    result2 = Peri(no1,no2)

    print("Area :",result1)
    print("Perimeter :",result2)

if __name__ == "__main__":
    main()