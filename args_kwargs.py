# *args and **kwargs tutorial
# *varss and **kars tutorial

# def function1(name,age,rollno):
#     print("The name of student is",name,"and age is",age,"rollno is",rollno)


from multiprocessing.sharedctypes import Value


def argsfunction(*args):
    print(type(args))
    print("The name of student is",args[0],"and age is",args[1],"rollno is",args[2])


def kwargfunction(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)


def mxfunction(normal,*args,**kwargs):
    print(normal)

    for i in args:
        print(i)

    for key,value in kwargs.items():
        print(key,value)

def main():
    # print("For args")
    list1 = ["Anil",23,4543]
    # argsfunction(*list1)
    
    # print("For kwargs")
    marklist = {"Anil":99,"Rahul":54,"rohit":99,"Raj":56}
    # kwargfunction(**marklist)

    normal = "Anil"
    mxfunction(normal,*list1,**marklist)


if __name__=="__main__":
    main()
 