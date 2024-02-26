#This is a program to find prime number within a given range of numbers
#Date : 26.02.2024
#Name : Kelsey Webb

start=int(input("Enter the starting point:"))
end=int(input("Enter the end point:"))

for number in range(start,(end + 1)):
    if number>1:
        for i in range(2,int(number**0.5)):
            if (number%i)==0 :
                break
        else:
            print(number)    


        























