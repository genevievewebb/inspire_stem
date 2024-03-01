#This is a program to find the surface area of different solids.
#Date : 29.02.2024
#Name : Kelsey Webb
import math

shape=str(input("Enter the desired solid:"))

if shape == ("cylinder"):
    radius=float(input("Enter the radius of the solid:"))
    height=float(input("Enter the height of the solid:"))

    def sa_cylinder(radius,height):
     diameter=(radius*2)
     return((math.pi * diameter * height) + (math.pi * (radius ** 2)))
    print(sa_cylinder(radius,height))

elif shape == ("cube"):
    side=float(input("Enter the length of one side:"))

    def sa_cube(side):
     return((side ** 2)*6)
    print(sa_cube(side)) 

elif shape ==("sphere"):
     radius=float(input("Enter the radius of the solid:"))

     def sa_sphere(radius):
      return((4/3)*math.pi*(radius**2))
     print(sa_sphere(radius))

else:
    radius=float(input("Enter the radius of the solid:"))
    slant_h=float(input("enter the slant height of the cone:"))

    def sa_cone(radius,slant_h):
       return((math.pi*radius*slant_h)+(math.pi*(radius**2)))
    print(sa_cone(slant_h,radius))    

















































