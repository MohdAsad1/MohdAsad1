"""
Created by Guido van Rossum and released in 1991 
Python is a popular, high-level, general-purpose programming language known for its simplicity and code readability.
Variusly used in web deveblemnet, Data Science , Data Analysis, Automation, AIML
"""
"""
{The benefits of using python}
1- [ Easy to use ] – Python is a high-level programming language that is easy to use, read, write and learn.
2- [ Interpreted language] – Since python is interpreted language, it executes the code line by line and stops if an error occurs in any line.
3- [ Dynamically typed ] – the developer does not assign data types to variables at the time of coding. It automatically gets assigned during execution.
4- [ Free and open-source ] – Python is free to use and distribute. It is open source.
5- [ Extensive support for libraries ] – Python has vast libraries that contain almost any function needed.
   It also further provides the facility to import other packages using Python Package Manager(pip).
6- [ Portable ] – Python programs can run on any platform without requiring any change.
7- It provides more functionality with less coding.
8- there are 68 build in functions in python:- like :- input(),object(),sorted().
9- machine learning, data science and its wealth of software libraries from the Python Package index (PyPI) that lend the language to those fields.
"""
# strings are Immutable(UNchangeable) and Iteratable(can be processed one after one,or we say it can be broken up into Elements) data types.
# lists are Mutable(Changeable) and strings sre Immutable (UNChangeable)

"""
# print("hello world 6")
"""

"""
remove
the
code
"""

#import operator
import random

"""
print("salman bhai",end=",")
print("king of bollywood")
print("c:asad")
"""

"""
var1= "45"
var2= 45
var3= 4.7
print(type(var2))
print(int(var1)+int(var2))
"""
VAriable name can not start with any number or a special character expect("_", like Exapmle = _name)

#Split Function

"""
x,y=input("Enter any two no with having space B/W them  ").split(" ")
print(int(x)+int(y))

"""

#print(100* "hellow world\n")
"""
print("enter your number")
inpnum=input()
print("you Entered",int(inpnum)+20)
"""

"""
print("Enter first number")
n1=input()
print("Enter secound number")
n2=input()
print("Sum of these two numbers is",int(n1) + int(n2))
"""
3 characterstics an String
1- immutable
2- indexed
3- iterable

#class 9 [SLICING]
string[start: stop: stepl
start = 0
stop = 3, exclusive 3, 
step - 1 2 3
text = "this is python the king of AI"
print (text [1:5:1])

# We can reverse a string by just string[::-1]

"""
mystr="harry is a dog who loves biscuit"
#print(mystr[0:87:2])
#print(len(mystr))
print(mystr.upper())
print(mystr.capitalize())
print(mystr.find("dog"))
print(mystr.count("o"))
print(mystr.replace("a","the"))

 # Swapcase will reverse Uppar Charecter to lower and lower to uppar

 # [split Function]
 srt = "new,three,yaar"
 Print(str.split(","))

 Result = ["new", "three", "yaar"]

 # [join(iterable)]
result = ", ".join(str)
print (result)

# .startwith("n") and .endswith("n") is used to check the starting and ending letter
# .isalpha("n") and .isdigit("n") is used to check the Alphabatic and Digit letters
# .isalnum("n") is used to check the  str contains both Alphabatic and Digit letters

# Array and List are same but the diff is List can contain diffrent data-Types in a list but Array can not contain data of diff datatypes

"""

"""
list=["asad","anas" ,"sadaf" ,"saifi","ji"]
print(list)
list.reverse()
print(list)
"""
"""
#concatenation
name = "sagar"
ser_name = "Khan" 
print ('Hi', name + ser_name)
"""
We use remove methord to directly remove the element like remove(name) and pop methord to remove the element from the location like list[0]

List = [mutable] ,tupple = (Immutable- can'nt be changed at runtime), set ={alike a list but can not contain repeated items, ex set{a,b,g,h,j}, Mutable}
Frizenset = {Immuatable set }
"""
numbers =[78,846,75,68,839]
numbers.append(64)
print(numbers)
"""

Python follows PEMDAS(BODMAS) rule in operations - Peranthesis {} > Exponants (3^{4}\) > Multiplication,Divide * / > Addition Substraction + -

a // b = Floord divison - Remove decimal value after divide 
a % b = modulus - give remander after divide
a ** b = a ki power b
"""
list=[64,37,85,96,7,4,92,94,67,65]
print(list)
list.insert(2,97)                                         # To insert perticular Element on a specified position
print(list)
list.remove(67)
print(list)
list.pop(7)
print(list)
"""

#mutable=can be change
#immutable=can not be change(tupple)
#swapping programe
"""

swap formate={temp=a
              a=b
              b=temp}

"""

"""
a=54
b=76
a,b=b,a
print(a,b)
"""
==========================================================================================================
# Finding the common elements of two list
a=[1,2,3]
b=[3,4,5]
#set function
s1 = set(a)
s2 = set (b)
s3 = s1.intersection(s2)   # give common from two lists
print(list(s3))
# output = [3]
===========================================================================================================
#Types of Copy in Python

1. Soft Copy (Shallow Copy)
Creates a new object, but does not recursively copy the inner objects.
original = [[1, 2], [3, 4]]
shallow_copy = copy.copy(original)  # Shallow copy

2. Hard Copy (Deep Copy)
Creates a completely independent copy of the object and all nested objects.
original = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original) 
===========================================================================================================

#dictonary function
# dictonery does not Support indexing

"""
d1={}
d2={"harry":"burger","asad":"meet","Nazim":"kawab"}
print(d2)
print(d2["asad"])
print(d2.copy())
d2["lion"]="jungle"
print(d2)
print(d2.keys())
print(d2.items())

# d2.popitems will remove the last item(key:value) pair
"""

#prog to search meaning of a word in dictonery

"""
d1={"set":"collection of words",
    "words":"collections of alphabet",
    "nown":"collection of name,objects and things"}
a=input("please enter any word from dictonery")
print(d1[a])
"""

#SET DATA STRUCTURES #show ONLY unique data.

"""
set={1,1,2,3,4,6,6,6,8,9,9,9}
print(set)
"""

"""
s={1,1,2,3,4,6,6,6,8,9,9,9}
s.add(2)
s.add(20)
l=[3,4,7]
t=[5,7,8]
print(s)
print(l)
print(t)
"""

control statements
conditionäl - if, elif, else
for while else suite
nested
infinite loop
pass
continue
break
assert return

#IF ELSE

"""

var2=50
var3=int(input("enter any third Number"))
if var3>var2:
    print("great")
elif var3==var2:
    print("Equal")
else:
    print("less")

"""

#QUIZ ON ELSE IF

"""
print("enter your age")
n=int(input())
if n==0:
    print("you are not born properly")
elif 1<n<18:
    print("you are not able to drive a vehical")
elif n==18:
    print("we can not deside you are able to drive or not")
elif 18<n<100:
    print("you can drive a vehicle easily")
else :
    print("you are dead")
"""
# Faulty calculator --> Design a calculator which will correctly solve all the problems except the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator and the two numbers as input from the user and then return the result.
"""


num1=int(input("Enter 1st Number"))
num2=int(input("Enter 2nd Number"))
operator=input("So what do you want to do with the given numbers?'+','-','*','/'")
if num1==45 and num2==3 and operator=='*':
    print("555")
elif num1==56 and num2==6 and operator=='/':
    print("4")
elif num1==56 and num2==9 and operator=='+':
    print("77")
elif operator=='+':
    plus=num1+num2
    print("result =",plus)
elif operator=='-':
    minus=num1-num2
    print("result =",minus)
elif operator=='*':
    mul=num1*num2
    print("result =",mul)
elif operator=='/':
    dev=num1/num2
    print("result =",dev)
else :print("try another Number")
"""

#17 For loop

"""
list= [int,float,"asad",5,7,8,9,56,976,68,975,764,987]
print(list)
for item in list:
    if str(item).isnumeric() and item>=6:
        print(item)
"""

#Dictnary
#dict={"alic":{"age"}}
"""
student={
    "male":["asad","anas","ali","nadeem"],
    "female":["sadaf","nagina","ruby","rinki"]
}
for key in student.keys():
    for name in student[key]:
        if "a" in name:
            print(name)
"""
#18 While loop
"""
i=0
while(i<500):
    if i%2==0:
        print(i)
    i=i+1
"""
"""
list=[]
while len(list)<5:
    name=input("enter the name to be added inside the list :- ")
    list.append(name)
print("list is full")
print(list)
"""
# Break and Continue Statement
 Continue works as a skip commemnt 

Pass statement make our code to runn , basically it does Nothing
"""
i=0
while(True):
    if i+1<5:
        i+i+1
        continue
    print(i+1,end=" ")
    if(i==44):
        break #Stop the loop
    i=i+1

    print(i)
    i=i+1
"""
# 23 SHORT HAND IN IF STATEMENT

"""

a=int(input("Enter A\n"))
b=int(input("Enter B\n"))
print("B is grater then A") if a<b else print("A is grater then B ")

"""

# 24 Functions And Docstring :-

"""
def function1(a,b):
    print("you are in a Function",a+b)
    return 0
def function2(a,b):

                    '''
                        This is a function is of Average And this comment is called docstring which is inside the function
                    '''
     print("Average of the given numbers is:",(a+b/2))
     return 0

v=function2(67,86)
print(v)
print(function2.__doc__)

"""
# 25 Try and Except Handling
"""
print("Enter Number 1")
num1 = (input())
print("Enter Number 2")
num2 = (input())
try:
    print("the sum of these two number is:",int(num1)+int(num2))
except Exception as e:
    print(e)
print("This line is very Important")
"""

# 26 Python Files Basics
"""
"r" - open file for Reading - Default
"w" - open file for writing
"x" - create file if not exist
"a" - Add more content to the File
"t" - text mode
"b" - binary mode
"+" - read and write
"""
# 27 python file

"""
f = open("hub.txt")
#content = f.read()
#print(content)
print(f.readline())
f.close()
"""

# 29 Write and Appendng to File.

"""
f = open("asad2.txt","a")
a=f.write("ghaziabad is my birth place\n")
print(a)
f.close()
"""

# handle read and write both

"""
f = open("asad.txt","r+")
f.write("ghaziabad is my birth place\n")
print(f.read())
f.write("anywhere")
f.close()
"""

# 30 Astrologer's Stars
# 31 seek and tell in python files

"""
f = open("hub.txt")
#print(f.tell())
print(f.read())
#print(f.tell())
f.seek(10)
print(f.readline())
f.seek(10)
"""

# 32 Using with block to open python files
"""
with open("hub.txt") as f:
    a = f.read()
    print(a)
    """

# 33 health MAnagemnet system
# 3 clints -harry,rohan ,hammad
# 35 recursive vs iteration:

# Iteration method
"""
def factorial_iterative():
    fac= 1
    for i in range(n):
        fac=fac*(i+1)
    return fac
print(factorial_iterative())
"""

#Random Function
                       #random.randint(a,b)......make a random choice b/w a to b
                       #random.randrange()
                        #random.sample([1,2,3,4,5,6,7,8],2)

#1 dimention array
"""
size=int(input("Input size of the array you want to create :- "))
arr=[]
print("Enter",size,"Elements:",end=" ")
for i in range(size):
    element=input("enter Element :- ")
    arr.append(element)
print("the elements are :- ")
for i in range(size):
    print(arr[i],end=" ")
"""

#two dimention array
"""
row_n=int(input("Enter No of row:  "))
col_n=int(input("Enter No of col:  "))
arr=[[0 for col in range(col_n)]for row in range(row_n)]
for row in range(row_n):
    for col in range(col_n):
        arr[row][col]=row*col
print(arr)
"""

# Implementation of stack using list
"""
stack=[]
stack.append("welcome")
stack.append("to")
stack.append("india")
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
"""

#Implementation of stack using Deque
"""
from collections import deque
stack=deque()
stack.append("asad")
stack.append("anas")
print(stack)
stack.pop()
print(stack)
"""

#Implementation of stack using queue
"""
from queue import LifoQueue
stack=LifoQueue()
stack.put("home")
stack.put("car")
stack.put("money")
print(stack)
stack.get()
print(stack)
stack.get()
print(stack)
"""

# difference in python 2 and python 3  :-
#when we devide any number in python 2 the answer will get the result in  an integer No. where as in python 3 answer will be flout by which we get Actual answer;
#strip is used to remove unwanted elements or spaces in a string or a variable [EX:--  .strip()]
#List Comprihension [method by which we can combine a variable ,a loop,and logic in a single line of code]

# Range Function
range (start, stop, step)
start - 1
stop - 100, exclude
step - 1
"""
a = list (range (1,10,1))
print(a)
"""
"""
even_number = [x for x in range(1,100+1) if(x%2==0)]
print(even_number)
print(len(even_number))
"""

"""
odd_number = [x for x in range(1,101) if(x%2!=0)]
print(odd_number)
print("the length of odd number from 1 to 100 is "+str(len(odd_number)))
"""

"""
word=["the","quick","brown","fox","jumps","over","the","dog"]
answer=[[i.upper(),i.lower(),len(i)] for i in word ]
print(answer)
"""

# join() method is used to join the different elements of the list to a single sentence
# FUNCTIONS
# function is a reuseable peace of code that gives us result
# difference b/w return and print [Print is only used to showcase the value onto the screen] // [return have there data type and store the data inside memory].

"""
def add(x,y):
    return x+y
a=add(56,45)
print(a)
"""

"""
def reverse(text):
   return text[::-1]
p=reverse("pen")
print(p)
"""

"""
def reverse(text):
   return text[::-1]
p=reverse([21,34,65,76])
print(p)
"""

"""
def reverse(text):
   return text[::-1]
p=reverse(str(56))
print(p)
"""

"""
def func(name,age,likes):
    a=print("my name is {} and my age is {} and i likes {}".format(name,age,likes))
    return (a)
func("asad",25,"python")
func(age=56,likes="java",name="anas")
"""

"""
def func(name,age,likes="python"):                                                           #defoult parameter [Always put default parameter at the last]
    a=print("my name is {} and my age is {} and i likes {}".format(name,age,likes))
    return (a)
func("asad",25,)                                                                             #run without full description
"""

"""
def func(name="asad",age=22,likes="python"):                                                 #defoult parameter [Always put defoult parameter at the last]
    a=print("my name is {} and my age is {} and i likes {}".format(name,age,likes))
    return (a)
func()
"""

#  variable scopes in python Global ,local
#  Every local can access the global variable

"""
a=150                                  # Global
def f1():
    global a
    a=100
    print(a)
def f2():
    b=564                               # local
    print(b)
f1()
f2()
print(a)
"""

#packing and unpacking variable

"""
def add(*numbers):                       # packing
    total=0
    for number in numbers:
        total=total + number
    return total
print(add(12,32,2349,45,56,67,787,231))
"""

"""
print(*"abcdef")                         # unpacking (ever element become individual)
"""

"""
def foo(**kwargs):                       # ** for keywords arguments
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))
a=foo(huda="female",ziad="male")
print(a)
"""

# ‘lambda()’ is a keyword in python which creates an anonymous function.
# Using *args to pass the variable length arguments to the function.

"""
def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:", sum)
adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)
"""

# Using **kwargs to pass the variable keyword arguments to the function

"""
def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
"""

"""
list= [int,float,"asad",5,7,8,9,56,976,68,975,764,987]
for i in list:
    print(i)
"""
