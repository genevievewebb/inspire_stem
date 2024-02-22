#this is a program to find the surface area of a cylinder
#Date= 20.02.2024
#Name= Kelsey Webb

r=float(input("Enater the radius of the circular face"))
pi=3.141592653589793

area_of_the_circle= pi*(r**2)

d=2*r
length_of_the_cylinder=pi*d
height=float(input("Enter the height of the cylinder"))

area_of_curved_surface= height * length_of_the_cylinder

total_surface_area= 2*(area_of_the_circle) + area_of_curved_surface

volume_of_the_cylinder=area_of_curved_surface * length_of_the_cylinder

print("The volume of the cylinder is :" , volume_of_the_cylinder)
print("The total surface area of the cylinder is :" , total_surface_area)
