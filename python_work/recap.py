#recap of level 2 python course
#print is how we display information in a terminal
print("this is my current file")

#greeting is a varible, print will print contents of the variable
greeting = "Hello World"
print(greeting)

#string = text
#boolean = true or false
#integer = whole number
#floating point = decimal number
#none = null - no value
print("hello this is a string")                         #string
print(True)                                             #boolean True or False, must have capital 
print(1234)                                             #integer
print(0.0002)                                           #floating point
print(None)                                             #no value - null

#methods used to manipluate data
print(len("hello world"))                               #len = length of string including speces
print(("hello world"[1]))                               #will return value of "e" indexing starts 0, [-1] will return last character
print(greeting.upper())                                 #.notation is a way of accessing methods 

#Libaries
from codecs import BOM_BE
from inspect import walktree
from logging.handlers import WatchedFileHandler
import random                                           #will import the random libary - should go at start of file
from random import Random,randint,uniform               #will import named methods from the random libary - should go at start of file
print(random.random())                                  #will return a random floating point number between 0 and 1
print(random.uniform(1,10))                             #will return a random floating point number between user defined values of 1 and 10
print(random.randint(1,10))                             #will return a random integer between user defined values of 1 and 10

#python uses snake_case, all lower letters and _ for spaces
#varibles
my_name = "Nick"
my_age = 35

print(my_name)
print("Hello my name is",my_name," and I am",my_age,"years old")            #will insert varibles inbetween the text with spaces
print("Hello my name is " + my_name)                                        #will insert varibles inbetween the text with string varibles
print("Hello my name is {} and I am {} years old".format(my_name,my_age))   #{} are filled in with varibles listed in order
print(f"Yo my name is {my_name} and I am {my_age} years old")               #f string alternative to above, easier to read and varibles in the flow

#Assignment opperators
#+ - addition
#- - subtraction
#* - multiplcation
#** - to power of
#/ - divide
#% - modus

print(1+2)
print(2-1)
print(2*3)
print(3**3)
print(15/3)
print(15%3)

balance = 100
amount = 50

print(balance-amount) 
balance = balance - amount                              #balance -=amount does same thing
print(balance)

char_name = input("What is your name?  > ")
print(f"welcome, {char_name}")

#if else        = assign, == equal to, != not equal to, >= greater than or equal, <= less than or equal
#if statements need if and else options as a minimum

music = "classical"

if music == "classical":
    print("oh no, it's classical music")
elif music == "pop":
    print("Turn it up")
else:
    print("Yay")

print(10%2==0)                                          #will return a boolean of True

num1=10
num2=20

if num1 > num2:
    print("number 1 is the bigger number")
elif num1 < num2:
    print("number 2 is the bigger number")
else:
    print("numbers are equal")


num = 14

if num%3==0:
    print("fizz")
elif num%7==0:
    print("buzz")
elif num%7==0 and num%3==0:                             #order of if statement important - this should be the first argument
    print("fizzbuzz")                                   #and operator, all must be true, or operator, one must be true
else:
    print(num)

#functions, def to clear function name, () hold parameters but still needed evne with out parameters

def light_switch():
    print("Who turned out the lights")

light_switch()

def cash_wtihdrawl(amount, accnum):                     #amount and accnum need to be stated when function called
    print(f"Withdrawing {amount} from account {accnum}")

cash_wtihdrawl(200, 56769060)

def add_up(num1,num2):
    return num1+num2

print(add_up(5,2))

#list, [] seperated by ,    not whitespace dependant but helps for reading

coffee_order = [
    "Alex - Cortado",
    "Ben - Latte",
    "Charlie - Whatsever's new"
]

print(coffee_order[1])                                  #zero indexed

coffee_order[2] = "water"

print(coffee_order)

#loops

for i in coffee_order:                                  #will run through list and print each item until all completed
    print(i)

for i in range(10):
    print(i)

for i in range(0,10,2):                                 #full version of previous with start,stop,step
    print(i)

num=0

while num <10:
    num +=1
    print("hello")