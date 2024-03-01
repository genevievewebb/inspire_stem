#Are a block of code running together as a unit.
#the are two types of functions(buillt-in and user-defined)

# Step 1-initialize/define a function(use a key word def.)
# Step 2-call the function

def print_name():
    print("My name is Kelsey Webb.")

#calling the function.
    
""""    
print_name()
print_name()
print_name()

def print_details(name,age,id_number,gender):
    print("my name is {0},{1} years old.My id number is {2} and my gender is {3}".format(name,age,id_number,gender))

print_details("Kelsey Webb","17","26383382","female")
print_details("Ivy Nyawira","17","26363636","female")  

"""

"""
def sum_nums(x,y):
    return (x + y)

z = sum_nums(10,20)
print(z)

def prod_nums(x,y):
    return(x*y)
print(prod_nums(10,15))

"""

def print_odds(first_no,last_no):
    for i in range(first_no,last_no):
        if (i % 2 == 1):
            print(i)
print_odds(0,10)

         


































