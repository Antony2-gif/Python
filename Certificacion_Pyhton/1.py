#Cual es la salida del siguinte codigo
#print("London",'Berlin','Rome',"end=" " ")


"""
#Pregranta 2
def capitans(**val):
    for country,capital_city in val.items():
        print("{}->{}".format(country,capital_city))

capitans(UK="London",France="Paris")
"""

#Pregunta 3

fruits = ("Apples","Oranges","Bananas")
fruit1,fruit2,fruit3 = fruits


print(fruit3)

#Pregunta 4
x = 5

def fun(x):
    x = x - (x-2)
    return x

print(fun(fun(fun(x-1))))

#Pregunta 5
tupl = ("bananas","apples","cherries")
print(sorted(tupl))

#ounput = ['apples', 'bananas', 'cherries']

#pregunta 6 
count = 0
for i in range(0,2):
    for j in range(0,2):
        count +=1
print(count)

#ountput: 2

#Pregunta 7

def fun(a,b=1,c=4):
    print(a+b+c)

fun(1,2)
fun(5,c=2)
fun(c=8,a=3)

#ounput = 7,8,12


#Pregunta 8

str1 = "Hello"
str2 = "HeLLo"
print(str1 == str2.capitalize())


#Pregunta 9
high_five = [10,0,5,15]
high_five.sort(reverse=True)
print(high_five)

#Pregunta 10
nums = [1,0]
for i in range(2):
    nums.insert(0,i)

print(nums)

#Pregunta 11
name1 = name2 = name3 = "Robert"
print(name3)

# Pregunta 12\\

#Pregunta 13

me = "apples",
print(me)

#Pregunta 14
lst = [x for x in range(3)]

print(lst)

#Print 15
x = 1
if(x>0):
    print("*")
    if x<2:
        print("*-")
    elif x==1:
        print("*+")
    else:
        print("*=")
else:
    print("*")

#Ejercicio 16
    

def squered(num):
    global sq
    sq = num ** 2
squered(5)
print(sq)

#Ejercicio 17
a = False
b = True

if a or b:
    print("True")
else:
    print("False")

#Ejericio 18

address_bok = {'name':"Robert",'age':'28',"city":"Dar"}