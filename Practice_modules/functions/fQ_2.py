'''Write a function func1() such that it can accept a variable length of arguments
and print all argument's value'''

def func1(**arguments):
    for i in arguments:
        print(arguments[i], end = "\t")

func1(a="adfd",b="2354435",c="aauuh",d="efwe")