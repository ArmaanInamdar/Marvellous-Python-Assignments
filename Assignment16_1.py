
def main():
    fobj = open("Student.txt",'w')
    fobj.write("rohit\n mohit\n surya\n rahul\n rohan")

    print("File created with student names")

if __name__ == "__main__":
    main()