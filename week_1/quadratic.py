#This is a program to solve quadratic equations
#Date: 20.02.2024
#Name:Kelsey Webb

a=float(input("Enter the coefficient of the first term : "))
b=float(input("Enter the coefficient of the second term : "))
c=float(input("Enter the constant"))

d=( (b**2) - (4*a*c) )

x_1=(-b + sqrt(d))/ 2*a
x_2=(-b - sqrt(d))/ 2*a

print("The solutions of the quadratic equation are:",x_1 |" and :",x_2)