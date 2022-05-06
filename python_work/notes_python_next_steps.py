#Converting data types
#create integer data type

# print(int(5.4))                                                         #floating point, int will round down, use round to round mathmatically
# print(int("54"))                                                        #string, convert number string to int

#print(int("bob"))                                                        #int cannot change letters to integer

# print(float(54))                                                        #float will convert to floating point decimal, adds .0 to number

# print(str(54.0))                                                        #str converts to string value

#^^ this process is called casting, very useful for user input

#improve if and else with truthy and falsy

# print("what is your name?")
# name = input()

# if name:
#     print(f"hello {name} ")
# else:
#     print("you did not provide a name")
    
#falsey values are empty, everything else is truthy

# print(not True)
# print(not False)

# bool = False
# if bool != True:
#     print(False)
# else:
#     print(True)
    
# bool = False
# if not bool:
#     print(False)
# else:
#     print(True)
    
#^^ both above give same result

from re import T


# def add_up():
#     num1 = input("enter first number    ")
#     num2 = input("enter second number   ")
#     print(num1 + num2)                                                               # + here is concatination 
    
# add_up()

# def add_up():
#     num1 = input("enter first number    ")
#     num2 = input("enter second number   ")
#     print(int(num1) + int(num2))                                                     # + here is addition 
    
# add_up()

# def add_up():
#     num1 = input("enter first number    ")
#     num2 = input("enter second number   ")
    
#     try:
#         print(f"{num1} + {num2} is {int(num1) + int(num2)}")
#     except:
#         print("Error")
#         print("You Muppet")
    
# add_up()

# light = False

# def light_switch():
#     global light                                                                        #global passes global variable into function
#     if light:
#         print("it's bright in here")
#         light = False
#     else:
#         print("who turned the lights off?")
#         light = True

# light_switch()
# light_switch()

#lists and tuples, tuples are collections of values but fixed

# even_nums = [2, 4, 6, 8, 10]

# odd_nums = (1, 3, 5, 7, 9)

# even_nums.append(12)
# even_nums.insert(0,0)

# for i in even_nums:
#     print(i)

# odd_nums.append(12)
# odd_nums.insert(10,0)
