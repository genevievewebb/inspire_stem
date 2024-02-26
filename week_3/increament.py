#This is a program to calculate the increament of an employee`s salary. 
#Date : 26.02.2024
#Name : Kelsey Webb

salary=float(input("Enter your current salary:"))

if (salary<=float("100000")):
    new_salary=(salary * 1.3)
    print("Your new salary is :" , new_salary) 

if (salary > float("100000") <= int("150000")):
    new_salary=(salary * 1.15)
    print("Your new salary is :" , new_salary) 

if (salary>float("150000")):
    new_salary=(salary * 1.1)
    print("Your new salary is :" , new_salary)    

  















