#This is a program to demonstrate loops.
#Date : 27.02.2024
#Name : Kelsey Webb

movies=["purple hearts","the pianist","me before you","the fault in our stars","five feet apart","the space between us"]
print(movies)

for _ in range(2):
    movies.pop(0)
    print("\n")
    print(movies)

movies.sort()
print("\n")
print(movies)

movies.reverse()
print("\n")
print(movies)

print("\n")
total_movies=len(movies)
print("The total number of movies available is:", total_movies)











































