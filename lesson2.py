""""
Name: Guoming Liao
Date: 9/24//24
Description: More on f-strings, input, and numbers/ops
"""

my_int = 5
my_float = 6.38

print(f"{my_int} {my_float}")

another_float = 8.0 # make this a float by adding .0
float_two = (float)(8) #make a float by casting
print(f"{another_float} {float_two}")

#get decimal from a user
radius = float(input("Enter a radius: "))
print(f"You entered a radius of {radius}")

# operations on numbers
# P M MModD AS
# modulus operator or remainder operator
print(15 % 7) # prints the remainder when 15 is divided by 7
print((2+3)*4) # 2+3 first, then times 4

# exponent is not ^, it is **
print(5**4) # this is 5^4, 5 to the 4th
print(5^4) #this is not

# weird
print(0.3-0.2) # roundoff error - watch out for it

# rounding
# method 1, use round()
num = 3.1415
print(round(num,2))
# method 2, use f string
print(f"{num:.2f}") # f for float

# ask user for some amount of US dollars
# store this in a variable
# convert that money to some currency of your choice
# store the conversion factor in a variable
# store the final amount in a variable
# print it like "___ USD is the same as ___ CAD".
# round to 2 decimal places
usd = float(input("Enter an amount of USD to convert into RMB: "))
conversion_factor = 7.01
rmb = usd*conversion_factor
rounded_rmb = round(rmb,2)
print(f"{usd} USD is the same as {rounded_rmb} RMB")

# string methods
name = "lee cat"
print(name.upper())
print(name.title())
print(name.lower())
