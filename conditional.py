# problem:
# -- movie tickets are prices based on on age
# 12$(for adult 18 or greater) and 8$ for child
# everyone gets 2$ discount on wednesday.
# ticket_price = 0
# day = "friday"
# age = 15

# # if age <= 18:
# #     ticket_price = 12
# # else:
# #     ticket_price = 8

# ticket_price = 12 if age >= 18 else 8
# if day == "wednesday":
#     ticket_price = ticket_price-2

# print("ticket price is: ", ticket_price)


# customize a coffee order "small", medium or large with
# an extra shot of expresso

# extraShot=input("Extra shot? (Y/n): ").strip().lower()
# options_list=["small", "medium", "large"]
# print("Options: ",",".join(options_list))
# coffeeSize=input(str("choose your size: ")).strip().lower()

# while coffeeSize not in options_list:
#     coffeeSize = input("Invalid, try again: ").strip().lower()

# if extraShot == "y" :
#     print( " your order has", coffeeSize, "sized coffee with extra shot")
# else:
#     print( " your order has", coffeeSize, "sized coffee without extra shot")


# find the year is leap year or not---

year =int(input("enter year to find it is leap or not : "))
leap_year=False

if (year % 4 == 0 and year % 100 != 0):
    leap_year=True
if leap_year:
    print (year, " is a leap year")
else:
    print( year, " is not a leap year")