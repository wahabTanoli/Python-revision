# ------- count positive numbers present in the list ----

# number = [1, 2, 3, 4, -1, -2, -5, -45, 88, -99, 0]
# countOfPositive = 0
# for n in number:
#     if n >= 0:
#         countOfPositive += 1

# print(countOfPositive)


# # ------- provide the sum of even number till the given number.
# number = 20
# numbers_list = []
# i = 0
# while i <= 20:
#     numbers_list.append(i)
#     i += 1

# sumOfEven = 0
# for n in numbers_list:
#     if n % 2 == 0:
#         sumOfEven += n
# print(sumOfEven)

# -------- make the tables from 1 to given number and skip 5:
# n=10
# for n in range( 1, n+1):
#     for k in range (1, 11):
#         print(n," * ",k," = ",n*k)

# --------- Reverse a string using a loop -----
# string="abcdefghijklmnopqrstuvwxyz"
# reversedStr=""
# for char in string:
#     reversedStr= char + reversedStr
# print(reversedStr)

# ---------- find the first non repeatitive character ------
# string= "tester"
# counts={}
# for char in string:
#     if char in counts:
#         counts[char]=counts[char]+1
#     else:
#         counts[char]=1
# for char in string:
#     if counts[char]==1:
#         print(char)
#         break

# for char in string:
#     if string.count(char)==1:
#         print(char)
#         break


# ---------- keep asking for input untill user give number between 1 and 10--
# while True:
#     number = int(input("enter any number: "))
#     if number >= 1 and number <= 10:
#         print("you entered the correct number")
#         break
#     else:
#         continue


# --------- find is this a prime number
number = 5
is_prime = True

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime=False
            print(number," is not prime")
            break
        else:
             print(number," is prime number")