# wap to ask the user to enter names of their 3 favorite movies and store them in a list

m1=(input("enter the name of first movie: "))
m2=(input("enter the name of second movie: "))
m3=(input("enter the name of thrid movie: "))
Movies=[m1,m2,m3]
print(Movies)
#both are true
movie=[]
m1=(input("enter the name of first movie: "))
m2=(input("enter the name of second movie: "))
m3=(input("enter the name of thrid movie: "))
movie.append(m1)
movie.append(m2)
movie.append(m3)
print(movie)

#this method also works
"""
movies=[]
movies.append(input("enter the name of the first movie:" ))
movies.append(input("enter the name of the second movie: "))
movies.append(input("enter the name of the third movie: "))
print(movies)
"""
