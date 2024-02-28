#This is a program to describe my favourite year
#Date : 28.02.24
#Name : Kelsey Webb

specs = {"year of production":"1969","color":"lilac","engine":"396 cubic-inch Turbo jet V8 ","mass":"3500lbs","power":"365-390hp",
         "acceleration rate":"0-96.6km\h in 7.2 seconds","fuel consumption":"MPG of 11.98"} 

print("\n")
print("The specifications of an Chevrolet Impala are:")
print("\n")

for key,value in specs.items():
    print(key)
    print(value)
    print("\n")

chi_car = specs.copy() 
print("The specs of her car are :" ,chi_car)   

















