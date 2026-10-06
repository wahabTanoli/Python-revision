# ------- find square root of a number-----
# def squareroot(num,power):
#     return num**power

# print(squareroot(6,3))

# -------- write a function that multiply two numbers ans also can multiply string -------
# def multiply(a,b):
#     return a*b
# print(multiply(3,4))
# print(multiply('a',5))


# ------- write a function that return both area and circumfernece of a circle given its radius -----
# import math

# def circle_area(r):
#     area = math.pi*r**2
#     circumference = 2*math.pi*r
#     return ({'area': round(area,3), 'circumference': round(circumference,3)})

# print(circle_area(3))


# --------********** Lambda Functions *********---------

# cube = lambda num,power: num**power
# print(cube(3,3))

# #  ----------****** write a function that takes variable number of arguments
# # and return their sum ******---
# sum_all = lambda *args: sum(args)
# print(sum_all(1,2,3,4,5,5,6,7,8,9,9))


#  ----------****** kwargs ******---
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print(print_kwargs(name='abdul',lastname='wahab'))


#  ----------****** yeild ******---
# create a function that generate even numbers till given limit;

# def even_num_gen(limit):
#     # li=[]
#     for i in range(2, limit+1, 2):
#         yield i
#         # return i
#     #   li.append(i)
#     # return li


# for num in even_num_gen(10):
#     print(num)


# # -----------****** Recurrsive function *******------------
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))



# --------****** Clousre and Scopes ******-----------
def f1(num):
    def actual(x):
        return x**num
    return actual

f=f1(2)
print(f(3))
        