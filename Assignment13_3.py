class Numbers:
    

    def __init__(self,A):   
        self.Value = A          

        
    def ChkPrime(self):
        for self.i in range(2,self.Value):
            if(self.Value % self.i == 0):
                return False
        return True

    def ChkPerfect(self):
       self.sum = 0
       for self.i in range(1,self.Value):
            if(self.Value % self.i == 0):
                self.sum = self.sum + self.i

       if(self.sum == self.Value):
           return True
       else:
           return False
       
    def SumFactors(self):
        self.sum = 0
        for self.i in range(1,self.Value):
            if(self.Value % self.i == 0):
                self.sum = self.sum + self.i

        return self.sum

    def Factors(self):
        self.l1 = []
        for self.i in range(1,self.Value):
            if(self.Value % self.i == 0):
                self.l1.append(self.i)

        return self.l1


def main():
    print("Enter value")
    no1 = int(input())
    obj1 = Numbers(no1)
    print("Prime :",obj1.ChkPrime())
    print("Perfect :",obj1.ChkPerfect())
    print("Sum factors :",obj1.SumFactors())
    print("Factors :",obj1.Factors())
    print("Enter value")
    no2 = int(input())
    obj2 = Numbers(no2)
    print("Prime :",obj2.ChkPrime())
    print("Perfect :",obj2.ChkPerfect())
    print("Sum factors :",obj2.SumFactors())
    print("Factors :",obj2.Factors())
    
    

if __name__ == "__main__":
    main()