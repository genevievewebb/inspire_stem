#This is a program to calculate the hire purchase cost of an item
#Date= 20.02.2024
#Name= Kelsey Webb

deposit=float(input("Enter the amount deposited:"))
installment=float(input("Enter the installment amount :"))
time=int(input("Enter the number of months"))

hp_price = (deposit) + (installment * time)
print("The hire purchase price is" , hp_price)
