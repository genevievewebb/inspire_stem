#this is a program to find the surface area and the volume of a sphere
#Date= 20.02.2024
#Name= Kelsey Webb

r=float(input("Enter the radius of the sphere :"))
pi=3.141592

surface_area_of_the_sphere=4/3 * (r**2) * pi 
volume_of_the_sphere= 4/3  * (r**3) * pi

print("The surface area of the sphere is :" , surface_area_of_the_sphere)
print("The volume of the sphere is :" , volume_of_the_sphere)