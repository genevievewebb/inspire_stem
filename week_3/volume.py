#This is a program to find the volume of different solids.
#Date : 29.02.2024
#Name : Kelsey Webb
import math

shape=str(input("Enter the desired solid:"))

if shape == ("cylinder"):
    radius=float(input("Enter the radius of the solid:"))
    height=float(input("Enter the height of the solid:"))

    def vol_cylinder(radius,height):
     return( height * (math.pi * (radius ** 2)))
    print(vol_cylinder(radius,height))

elif shape == ("cube"):
    side=float(input("Enter the length of one side:"))

    def vol_cube(side):
     return(side ** 3)
    print(vol_cube(side)) 

elif shape ==("sphere"):
     radius=float(input("Enter the radius of the solid:"))

     def vol_sphere(radius):
      return((4/3)*math.pi*(radius**3))
     print(vol_sphere(radius))

else:
    radius=float(input("Enter the radius of the solid:"))
    vertical_h=float(input("enter the vertical height of the cone:"))

    def vol_cone(radius,vertical_h):
       return((1/3)*(math.pi*(radius**2)*vertical_h))
    print(vol_cone(vertical_h,radius))    
