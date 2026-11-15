#converting lists into dictionaries
keys= ["Ten","Twenty","Thirty"]
values= [10,20,30]
keys_values= dict(zip(keys,values))
print (keys_values)

#cinemax 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total= 0
for age in family.values():
    print (age)
    if age <3:
       total= total +0
    elif age <=12:
       total =total +10
    else:
       total = total +15
print("Total:", total)

#zara

brand= {"name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": "men, women, children, and home",
    "international_competitors": "Gap, H&M, Benetton",
    "number_stores": 7000,
    "major_color":{
        "France": "blue", 
        "Spain": "red", 
        "US": "pink,green"
     }
       
  }
print (brand)

brand ["number_stores"]= 2
print (brand)

print ("Zara has a variety of products for", brand ["type_of_clothes"])
brand ["country_creation"]= "Spain"
print (brand)

if "international_competitors" in brand:
    brand["international_competitors"] += ", Desigual"
print (brand["international_competitors"])

print (brand)
brand.pop("creation_date")
print (brand)

print (brand["international_competitors"].split(", ")[-1])
print (brand["major_color"]["US"])

print(len(brand))     
print (brand.keys())

#4 Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
user_indices= {}
user_indicess= {}
indices_user= {}
for user in users:
    user_indices[user] = users.index(user)
print (user_indices)

for user in users:
    user_indicess[users.index(user)]= user
print (user_indicess)

users.sort()
for user in users:
    indices_user[user] = users.index(user)
print (indices_user)
