#exercise 1 What are you learning?
def display_message():
    print("I am learning about functions in Python.")   

display_message()

#exercise 2 Whats Your Favorite Book?
def favorite_book():
    return input("One of my favorite books is: ")

favorite_book()

#exercise 3 Some Geography
def describe_city(city, country= "Unknown Country"):
    print(city, " is in ", country)

describe_city("Guayaquil")

#exercise 4 Random
import random

def random_number():
    return random.randint(1, 100)

def comparison(user_number):
    generated_number = random_number()
    if generated_number == user_number:
       print("Suceces!")
    else:
        print ("Fail")
        print ("user number is: ", user_number)
        print ("random number is: ", generated_number)

comparison (2)

#exercise 5 Lets Create Some Personalized Shirts!

def make_shirt(size= "large", message= "I love Python"):
    print(f"The shirt is {size} and says '{message}'.")
make_shirt()
make_shirt("Medium")
make_shirt("Small", "Python is awesome!")
make_shirt(size= "xs", message= "I love coding!")

#exercise 6 Magicians
magician_names= ["Harry Houdini", "David Blaine", "Criss Angel"]
def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)
def make_great(magician_names):
    for i in range (len(magician_names)):
        magician_names[i] = magician_names [i] + " the Great"
make_great(magician_names)
show_magicians(magician_names)

#exercise 7 Temperature Advice
def get_random_temp():
    return random.uniform(-10, 40)

def main():
    random_temp= get_random_temp()
    print (f"the temperature right now is {random_temp:.1f} degrees Celsius")
    if random_temp < 0:
      print ("Brr, thats freezing! Wear some extra layers today.")
    elif random_temp >16 and random_temp <23:
      print ("Quite chilly! Dont forget your coat")
    elif random_temp > 24 and  random_temp < 32:
        print("A bit war,. stay hydrated")
    elif random_temp > 32 and random_temp < 40:
        print ("Its really hot! Stay cool")

main ()

   
    

