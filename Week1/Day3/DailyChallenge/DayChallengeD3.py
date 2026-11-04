
def birthday():
    birthday = input("what is your birthday? (DD/MM/YYYY): ")
    print("      ___iiiii___")
    print("     |:H:a:p:p:y:|")
    print("   __|___________|__")
    print("  |^^^^^^^^^^^^^^^^^|")
    print("  |:B:i:r:t:h:d:a:y:|")
    print("  |                 |")
    print("  ~~~~~~~~~~~~~~~~~~~")

def sum(num: int, num2: int):
    return num + num2

def change_name():
    name = input("what is your name? ")
    print("hello " + name)
    
def number_zero():
    number = int(input("enter a number: "))
    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
        print("zero")
        
birthday()
print(sum(6, 7))
change_name()
number_zero()