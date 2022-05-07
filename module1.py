import os


def printName():
    print("Anil")
    print("Only print name")

def main():
    # print(os.listdir("/"))
    printName()
    print("It should not be printed in other module")
    
if __name__=="__main__":
    main()