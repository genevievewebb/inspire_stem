#This is a program to find the squares and cubes of numbers within a given range.
##Date : 29.02.2024
#Name : Kelsey Webb

x=int(input("Enter the starting value:"))
y=int(input("Enter the end point:"))

def numbers(x,y):
    for numbers in range(x,y):
        square=(numbers**2)
        cube=(numbers**3)
        print(str(numbers)+"\t",end=" ") 
        print(str(square)+"\t",end=" ") 
        print(str(cube)+"\t",end=" ") 
        print("\n")

print(numbers(x,y))













