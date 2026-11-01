my_fav_numbers = {3, 4, 7,8, }
my_fav_numbers.add(6)
my_fav_numbers.add(10)
print(my_fav_numbers)
my_fav_numbers.remove(10)
friend_fav_numbers = { 2, 18, 21, 50}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
print(sorted(our_fav_numbers))

#exercise 2
tuple= (1, 3, 4, 7)
tuple= (1, 3, 4, 7) + (2, 5)
print (tuple)
tuple= tuple + (2,5 )
print (tuple)


#exercise 3
methods= ["append","remove","insert","count","clear"]
print (methods)
methods.remove("remove")
methods.remove("append")
methods.append("divide")
methods.append("multiply")
methods.insert(0, "count")
count_count= methods.count("count")
print (count_count)

methods.clear()
print(methods)


#exercise 4
numbers= []
num=1.5
while num <= 5:
    numbers.append(num)
    num += 0.5
print (numbers)

list4= []
for i in range (3, 11):
    list4.append(i/2)
print (list4)

list4= [i/2 for i in range (3,11)]
print (list4)

list5= []
i= 1.5
while i <= 5:
    list5.append(i)
    i += 0.5
print (list5)

#exercise 5
for i in range (1,21):
    print (i)
    
#exercise 6
while True: 
    name= input("Enter your name: ")
    if len (name) >=3 and not name.isdigit():
        print ("thank you") 
        break
    else: 
        print ("enter different name")

#exercise 7
frutis= input ("Enter your favorite fruits:").split()
print (frutis)
any_fruit= input ("enter fruit:")
if any_fruit in frutis:
    print ("you chose one of yourfavorite fruits")
else:
    print ("you chose a new fruit, hope you like it")
    

#exercise 8

toppings= []
total =10
while True:
    topping =input ("enter pizza toppings and type quit when done: ")
    if topping == "quit":
      break

    toppings.append(topping)
    total = total +2.50
    print ("adding", topping, "to your pizza")
print ("your toppings:", toppings)
print ("total price : $", total)
        
#exercise 9
#ticket prices
price1 = 0
price2 = 10
price3 = 15
total_price=0 

family_members= input("how many are in your family: ")
print (family_members)
family_ages= input("enter all family ages: ").split()
print (family_ages)
for age in family_ages:
    age = int(age)
    if age <= 3:
        total_price += price1
    elif age <= 12:
        total_price += price2
    else:
        total_price += price3
print ("total price for the tickets: ", total_price)
