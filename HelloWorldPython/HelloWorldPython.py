#this is like a using statement in c#
from datetime import datetime, time, timedelta

# two pound signs next to each other are multiline comments.
# Operators are as follows:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ** is like mod
# #

##This is my first true python script.


#capturing input from the screen and storing them in variables.
first_name = input("What is your First Name? ") #capturing first name
last_name = input("What is your Last Name? ") #capturing last name
rando = int(input("Type in a random number: ")) #capturing a random number from the user
reverseStr = first_name[::-1] #reverse the first name given
print(reverseStr)

#concat the strings
print(first_name + " " + last_name)

#String methods
print("My First name using .upper is: " + first_name.upper())
print("My First name using .lower is: " + first_name.lower())
print("My First name using .capitalize is: " + first_name.capitalize())

#string.format functions
output = "Hello, my name is {0} {1}".format(first_name, last_name)
print(output)

#numeric data types
pi = 3.14159
print(pi)

for x in [first_name]:
    print(x)
    pass

first_num = 6
second_num = 5
print(first_num * second_num)
print(first_num - second_num)
print(first_num * second_num)
print(first_num / second_num)
print(first_num ** second_num)

#type conversion on numbers
print("Rando Number is " + str(rando))

#dates
current_date = datetime.now()
current_TimePeriod = timedelta(1)
yesterday = current_date - current_TimePeriod
print("Today is: " + str(current_date))
print("Yesterday was: " + str(yesterday))
print("Today is: " + str(current_date.day))

birthday = input("What is your birthday? (mm/dd/yyyy) ")
birthday_date = datetime.strptime(birthday, '%m/%d/%Y')
print("Birthday: " + str(birthday_date))

class Nameinfo():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    pass

class GetNameInfo(Nameinfo):
    def __init__(self):
        Nameinfo.__init__(self)
pass
