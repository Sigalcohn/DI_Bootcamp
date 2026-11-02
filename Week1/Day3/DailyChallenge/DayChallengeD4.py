#create a list of multiples of a given number up to a specified length
number= int(input ("enter a number: "))
length= int(input ("enter a lenght: "))
list= []
i = 1
while i <= length:
    list.append (number * i)
    i +=1
print (list)

#remove consecutive duplicate letters
word= input ("enter something: ")
new_word= ""
i= 1
for i in range (len(word)):
    if word [i] != word [i-1]:
        new_word += word [i]
print (new_word)

print ("hello ")


