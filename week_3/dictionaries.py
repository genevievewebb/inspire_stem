#Helps to model real items.
#Have a key value pair

my_laptop={"make":"HP","colour":"silver","weight":"900 grams","year":"2024"}

print(my_laptop["make"])
print(my_laptop["colour"])
print(my_laptop["year"])
print("\n")

my_laptop["colour"]="green"
my_laptop["year"]="2021"
my_laptop["size"]= "12.9in x 8.2in"
print(my_laptop)

"""""
for key,value in my_laptop.items():
    print(key)
    print(value)
    print("\n")
""""" 
del my_laptop["colour"]
print(my_laptop)

christy_laptop=my_laptop.copy()
print(christy_laptop)
