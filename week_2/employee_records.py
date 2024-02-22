#This is a program to calculate salary of an employee
#Date : 21.02.2024
#Name : Kelsey Webb

employee_name=str(input("Enter your first and surname:"))
employee_age=str(input("Enter your age:"))

employee_post=str(input("Enter your post:"))

if(employee_post==("manager") or ("auditor") or ("accountant")):
  salary=75000
  bonus=20000
  new_salary= float( (salary) + (salary * 0.3 ))
  new_bonus = float( (bonus) - 5000)
  total_monthly_income= (new_salary) + (new_bonus)
 
else:
  salary = (45,500)
  bonus = (10,000)
  new_salary = float((salary) + (salary * 0.3 ))
  new_bonus= float( (bonus) - 5000)
  total_monthly_income = (new_salary) + (new_bonus)


print("The employee`s name is :" , employee_name)
print("The employee`s age is :" , employee_age)
print("The employee`s post is :" , employee_post)
print("The employee`s new salary is :" , new_salary)
print("The employee`s new bonus is :" , new_bonus)
print("The employee`s gross income is :" , total_monthly_income)
































