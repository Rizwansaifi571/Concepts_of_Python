"""       ---> Exception Handling in Python <---       """

# a=input("Enter the number for multiplication table :")
# print(f'\nMultiplication table of {a} is')
# try:
#     for i in range (1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print(e)
# try:
#     print(int(a)*2)
# except Exception as e:
#     print(e)


"""       ---> Match_case Statemnet <---       """


# x=int(input("Enter X :"))
# match x:
#     case 0:
#         print(x)
#     case _ :
#         print("defaut")



"""       ---> Finally clause in python <---       """



# def fun():
#     try:
#         x=int(input("Enter no. :"))
#         print(x)
#         return 1
#     except:
#         print("wrong input!")
#         return 0
#     finally:
#         print("I am good")
# print(fun())


# def fun():
#     try:
#         l=[1,5,6,7]
#         i=int(input("enter the index :"))
#         print(l[i])
#         return 1
#     except:
#         print("some error occured!")
#         return 0
#     finally:
#         print("I am always executed!!")
# print(fun())
# fun()

# a=input("Enter any value between 5 and 9 :")
# try:
#     # a=str(a)
#     if a=="quit":
#         print("Enery thing is ok!")
# except:
#     if (int(a)<5 or int(a)>9):
#         raise ValueError ("Value shold be between 5 to 9")
#     print(a)
   
"""       ---> Raising Custom Errors <---       """

# a=int(input("Enter the value of a :"))
# class timeoutError (Exception):
#     if a>10:
#         print(a)
#     pass
# try:
#     if a==10:
#         print("b")
# except:
#     print("c")

# class MyCustomException(Exception):
#     def __init__(self, message):
#         super().__init__(message)

# # Example of raising and handling the custom exception
# def divide(a, b):
#     if b == 0:
#         raise MyCustomException("Division by zero is not allowed")
#     return a / b

# try:
#     result = divide(10, 0)
# except MyCustomException as e:
#     print(f"Custom Exception: {e}")
# else:
#     print(f"Result: {result}")



"""       ---> Enumerate Function in For Loop <---       """


# marks=[12 ,56 ,32 ,98 ,12]
# for index,mark in enumerate(marks):
#     print(index,mark)
#     if index==3:
#         print("Rizwan ! awesome!!")

# x=int(input())
# while x<0 in enumerate:
#     print("HElloe")
#     x+=1

# fruits=["apple","banana","grapes"]
# for c in enumerate(fruits):
#     print(c)

# fruits=["apple","banana","grapes"]
# for index,fruit in enumerate(fruits,start=1):
#     print(index,fruit)

# num=int(input("what is your table number :"))
# for p in range (1,11):
#     print(num,"x",p,"=",num*p)



"""       ---> How Import Works in Python <---       """


# import math
# result=math.sqrt(16)
# print(result)

# from math import pi,sqrt as s
# result=s(9)*pi
# print(result)

# import math as m
# result=m.sqrt(9)*m.pi
# print(result)

# import math
# print(dir(math))
# print(type(math.pi))
 
# import math
# print(math.sqrt(9))


"""       ---> File Handling in Python <---       """



# f=open("my file.txt","w")
# content=f.write("RIZWAN is a GOOD person")
# f.close()

# f=open("my file.txt","r")
# content=f.read()
# print(content)

# f=open("my file.txt","a")
# content=f.write(" I am inside")
# f.close()

# with open("my file.txt","r")as f:
#     c=f.read()
#     print(c)

# with open("my file.txt","w")as f:
#     c=f.write("I am a good boy!")
    # print(c)



# f=open("myfile.txt",'w')
# lines=["line1\n","line2\n","line3\n"]
# f.writelines(lines)
# f.close()

# with open("myfile.txt","r") as f:
#     f.seek(10)
#     data=f.read(5)
#     print(data)

# with open("myfile.txt","r") as f:
#     data=f.read(10)
#     current_position=f.tell()
#     f.seek(current_position)
#     dat=f.read(5)
#     print(data)
#     print(current_position)
#     print(dat)

# with open("sample.txt","w") as f:
#     f.write("I am very Inteligent")
#     f.truncate(15)

# with open("sample.txt","r") as f:
#     print(f.read())


"""       ---> Map , Filter and Reduce <---       """


# number=[1, 2, 3, 4, 5]
# double=filter(lambda x:x*2,number)
# print(list(double))

# number=[1, 2, 3, 4, 5]
# even=filter(lambda x:x%2==0,number)
# print(list(even))

# number=[1, 2, 3, 4, 5]
# even=map(lambda x:x%2==0,number)
# print(list(even))

# number=[5, 6, 8, 74, 9, 57 ,54]
# grt=filter(lambda x : x>9 ,number)
# print(list(grt))

# from functools import reduce
# number=[1, 2, 3, 4, 5]
# sum=reduce(lambda x,y : x+y , number)
# print(sum)


"""       ---> "is" vs "==" in python <---       """


# a=[1, 2, 3]
# b=[1, 2, 3]
# print(a==b)
# print(a is b)

# a="hello"
# b="hello"
# print(a==b)
# print(a is b)

# a=None
# b=None
# print(a==b)
# print(a is b)



"""       --->   Random Module In Python   <---       """


# import random
# a=random.random()
# print(a)

# import random
# a=random.randint(1,10)
# print(a)

# import random
# a=random.uniform(1,10)
# print(a)

# import random
# a=random.randrange(1,10,3)
# print(a)

# import random
# a=random.choice([1,True,2.5,"a","b","c"])
# print(a)

# import random
# a=["a","b","c",1,2,2.5,True]
# random.shuffle(a)
# print(a)

# import random
# a=random.sample(range(10,30),5)
# print(a)


"""       --->  <---       """