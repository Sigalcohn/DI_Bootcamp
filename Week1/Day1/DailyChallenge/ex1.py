#exercise 1
print ("Hello, World\n" * 4, end="")
#exercise 2
result= (99 ** 3) * 8 
print (result)
#excercise 3  
7 < 5  # False
print (7 < 5)
#exercise 4
computer_brand= "Microsoft"
print (f"I have a {computer_brand} computer")
#exercise 5
name= "Sigal"
age= 24
shoe_size= 37.5
info= f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}"
print (info)
#exercise 6
a= 10
b= 8
if a > b:
    print("Hello World")
#exercise 7
input_number= input ("choose a number: ")
if int(input_number) % 2 == 0:
    print ("The number is even")
else:
    print ("The number is odd")
#exercise 8
name= "Sigal"
user_name= input ("What is your name? ")
if user_name.lower() == name.lower():
    print ("You copied my name!")
else:
    print ("You copied someone else's name!")
#exercise 9
user_height= int (input ("What's your height in cm? "))
if user_height > 145:
    print ("congrats, you can ride the rollercoaster!")
else:
    print ("Sorry, you need a few more cm to ride")
    
#Daily Challenge
string_user= input ("Write something: ")
lenght= len(string_user)
if lenght < 10:
    print ("String not long enough")
elif lenght > 10:
    print ("String too long")
else:
    print ("Perfect string")
    print ("first character:", string_user[0])
    print ("last character:", string_user[-1])
for i in range (1,11):
    print (string_user[:i])
    

