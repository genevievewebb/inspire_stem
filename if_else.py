#This is a program that runs on if-else loops
#Date : 26.02.2024
#Name :



age=int(input("Enter your current age"))

if ( age > 18):
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")    

#this is a program to find the raise of certain employees.
salary=float(input("Enter current salary:"))
if (salary <= 40000):  
    print("You are not eligible for a raise.")  
else:
    new_salary=(salary * 1.1)
    print("Your new salary is :" , new_salary)

home_county=str(input("Enter county of origin"))
if (home_county == ("Turkana") or ("Garissa") or ("Wajir")):
    print("You are eligible for a bursary.")
else:
    print("You are not eligible for a bursary.")    

cluster_points=float(input("Enter your cluster points"))
if (cluster_points > 37.09):
    print("You are eligible for the course.")
elif (cluster_points <= 35.95 ):
    print("Please see Dean for an interview.")    


