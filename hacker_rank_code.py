# n=eval(input("ENTER A NUMBER 'N' :"))
# if n%2!=0:
#     print("Weird")
# elif n%2==0 and n in range (2,5):
#     print("Not Weird")
# elif n%2==0 and n in range(6,20):
#     print("Weird")
# elif n%2==0 and n>20:
#     print("Not Weird")

# n=int(input())
# for n in range (0,n):
#     print(n**2)

# def is_leap(year):
#     if (year%4==0 and year%100!=0) or (year%400==0) :
#         return True
#     else:
#         return False

# year = int(input())
# print(is_leap(year))

# n=int(input())
# for n in range(1,n+1):
#     print(n,end="")

# x = int(input("x"))
# y = int(input("Y"))
# z = int(input("z"))
# n = int(input("n"))
# def function():
#     for x in range (0,x+1):
#         print([x,y,z],end=",")
#     for y in range (0,y+1):
#         print([y,x,z],end=",")
#     for z in range (0,z+1):
#         print([z,x,y],end="")
# function.sort(print)

# x, y, z, n = [int(input()) for _ in range(4)]

# coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

# print(coordinates)


# x = int(input("Enter the value of x: "))
# y = int(input("Enter the value of y: "))
# z = int(input("Enter the value of z: "))
# n = int(input("Enter the value of n: "))

# coordinates = []

# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if i + j + k != n:
#                 coordinates.append([i, j, k])

# print(coordinates)

# lis1=[]
# for i in range(int(input("i"))):
#     a=int(input("a"))
#     lis1.append(a)
# a=max(lis1)
# lis1.remove(max(lis1))
# b=max(lis1)
# if a==b:
#     lis1.remove(b)
# else:
#     print(b)
# print(max(lis1))

p=int(input())
a=list(map(int(input()))).split().strip()
print(a)
b=max(a)
a.remove(max(a))
c=max(a)
while b==c:
    a.remove(max(a))
    break
print(max(a))