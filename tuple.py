""" it is a collection of items/elements/values theyare enclosed within the paranthesis or open brackets() separated by (,).
as tuple are immutable it mean we cant charge so when the data is fixed we can go with tuples"""
mytuple=(12,13,11)
print(type(mytuple))
mytuple1=()
print(type(mytuple1))
mytuple2=(10)
print(type(mytuple2))

#creation of tuple
mytuple3=(12,23,45,34+56j,[12,23,34],"hello",(123,"ece"))
print(mytuple3)

#creation of tuple with a single element
mytuple4=(45,)
print(type(mytuple4))

#creating tuple with a list
t=[4,45,43,"jj"]
print(t)
k=tuple(t)
print(k)

#creation of tuple with "tuple" predefine word
t=tuple()
print(t)

#accesing the elements in a tuple
mytuple5=(11,33,44,55,66,(67,87),"hello")
print(type(mytuple5))
print(mytuple5[0:3])
print(mytuple5[0:6])

mytuple6=([1,5,8,9],(2,3,4,7))
print(mytuple6[0])
print(mytuple6[1])
"""
#slicing:used to retrive the elements"""
mytuple7=(33,44,55,77,12,66,(67,87),"hello","ece","mech","agri")
print(mytuple7[0:11:3])
print(mytuple7[4:10:5])

mytuple8=(33,44,55,77,12,66,(67,87),56.87,44+6j,"dept",53,11,32,98,90,"hello","ece","mech","agri")
print(mytuple8[-11])
print(mytuple8[9:-1:2])