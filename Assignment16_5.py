
def main():
      
    fobj =  open("data.txt", 'r')
    data = fobj.readlines()
    for i in data:
        words = i.strip().split()
        if(len(words) > 5):
             print(i,end = '')
             

if __name__ == "__main__":
      main()