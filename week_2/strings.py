# STRINGS IN PYTHON 
# Date : 22.02.24
# Name : Kelsey Webb

city = "nairobi"

#this is used to separate characters in the string
#negative indices are used to reverse the order of characters in a string
#if a index is greater than the final index of the string,an error is seen because the index is out of range

print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])
print(city[5])
print(city[6])

#convet to uppercase
print(city)
print("\n")  #prints a new line
print(city.upper()) #converts string to uppercase

name="KELSEY WEBB"
print(name)
print(name.lower()) #converts strings to lowercase

town=" Naivasha "
print(town)
print("\t") #used to print a new tab
print(town.strip())

#It is possible to add two strings
f_name="Kelsey"
s_name="Webb"
full_name=f_name+s_name
print(full_name)

#REPLACING A CHARACTER
fruit="orange"
print(fruit.replace('a' , ' i'))


subject="physics,geography"
print(subject.split(","))

age=30
height=1.1

print("I am {0} years old and {1} metres tall " .format(age,height) )





