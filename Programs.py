# Program to reverse a string without inbuild function−
"""
my_string=("Nitesh Jhawar")
str=""
for i in my_string:
    str=i+str
print("Reversed string:",str)
"""

# palandrom No: [Front and reverse is Equal]
"""
num=input("Enter any number")
rev=num[::-1]
if(num==rev):
    print("no is palandrom")
else:
    print("not a palandrom")
"""

# HIDDEN GAME
"""
a=18
numbers_of_gusses=1
print("guess The number you think computer choose for you.you have only 10 chances")
while(numbers_of_gusses<=10):
        n=int(input("Guess the number:\n"))
        if int(n)<int(a):
          print("your number is smaller then the computer's choice")
        elif int(n)>int(a):
          print("your number is Greater then the computer's choice")
        else:
            print("you won\n")
            print(numbers_of_gusses, "No of guesses you take to make correct choice")
            break
        print(10 - numbers_of_gusses, "No of guesses left")
        numbers_of_gusses=numbers_of_gusses+1
if(numbers_of_gusses>=10):
    print("game Over You lose ")
"""

# display the multiplication table
"""
num=int(input("the number"))
for i in range(1,10+1):
    print(num,"*",i,"=",num*i)
"""
# [numbers divisible by another number]
"""
my_list = [12, 65, 54, 39, 102, 339, 221]
a=int(input("enter any num - "))
result = list(filter(lambda x: (x % a == 0), my_list))                              # lambda nameless function for a short period of time
print("Numbers divisible by ",a,"are",result)
"""
# mean of the List of array

"""
from statistics import mean
Estimates =[100,36,89,457,65,998,98,6451,89,65,89,65,78,87,65,54]
print(Estimates)
Estimates.sort()
for i in range(len(Estimates)):
    print(Estimates[i])
tv=int(0.1*(len(Estimates)))

Estimates=Estimates[tv:]                            #remove the first 10% Elemenets
for i in range(len(Estimates)):
    print(Estimates[i])
Estimates=Estimates[:len(Estimates)-tv]             #remove the Largest 10% Elemenets
print(mean(Estimates))

"""
# Deleting the Element from array
"""
size=int(input("enter the size of the array you want to develop :"))
arr=[]
print("input the " +str(size)+" Elements in the Array :")
for i in range(size):
    arr.append(input())
print("the given Array was")
print(arr)
val=input("Now Enter the no you want to Delete ")
if val in arr:
    arr.remove(val)
    print("the new array is :")
    print(arr)
else:
    print("The Element was not present inside the given array")
"""
# sorting the Elements of the array
"""
size=int(input("enter the size of the array you want to create "))
arr=[]
print("enter the "+str(size)+ " elements of the array")
for i in range(size):
    arr.append(input())
print("the given array is")
for i in range(size):
    print(arr[i])
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i] > arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print()
print("the Array after sorting: ")
for i in range(0,len(arr)):
    print(arr[i])
"""
# [vowels and consonents program]

"""
vowels=0
consonents=0
a=input("Enter any string")
for letter in a:
    if letter.lower() in "aeiou":
        vowels=vowels+1
    elif letter==" ":
        pass
    else:
        consonents=consonents+1
print("there are {} vowels".format(vowels))
print("there are {} consonents".format(consonents))
"""
# HCF of two numbers
"""
def hcf(a,b):
    if a>b:
        smaller=b
    else:
        smaller=a
    for i in range(1,smaller+1):
        if((a%i==0) and (b%i==0)):
            common =i
    return common
n1=int(input("Enter First number"))
n2=int(input("Enter secound number"))
print("the HCF from Both Numbers are",hcf(n1,n2))
"""
# factors of a number         --> the list of number by which our number is devisible <--
"""
def fec(x):
    for i in range(1,x+1):
        if x % i ==0:
            print(i)
fec(80)
"""
# Calculator using Functions
"""
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
"""
# Program to add two matrices using nested loop
"""
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)
"""

# Program to transpose a matrix using a nested loop
"""
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
for r in result:
   print(r)
"""

#prog two multiply two matrix
"""
x=[[23,43,45],
   [34,34,65],
   [23,54,76]]
y=[[21,54,76],
   [67,98,43],
   [32,54,76]]
o=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            o[i][j]=x[i][k]*y[k][j]
for r in o:
    print(r) 
"""
# [prog to sort the words of the string in Alphabetic Order]
"""
str="the quick  Brown fox jumps over the litle baby lazy dog"
words = [word.lower() for word in str.split()]
words.sort()
for word in words:
    print(word)
"""
#program to ADD elements of two lists into a single list
"""
l1=[]
l2=[]
l3=[]
for i in range(1,6):
    if i==4 or i==5:
        l1.append(0)
    else:
        a = int(input())
        l1.append(a)
print([l1])
for i in range(1,6):
    b=int(input())
    l2.append(b)
print(l2)
for j in range(5):
    l3.append(l1[j]+l2[j])
print(l3)
"""
# Program to print half pyramid using *
"""
row=int(input("enter the rows "))
for i in range(row):
    for j in range(i+1):
        print("*",end="")
        print("\n")
"""
# Program to print half pyramid using alphabets
"""
row=int(input("Enter the row "))
ascii_value=65
for i in range(row):
    for j in range(i+1):
        alphabet=chr(ascii_value)
        print(alphabet,end=" ")
    ascii_value+=1
    print("\n")
"""
# Program to print full pyramid using *
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
"""
rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")
    while k != (2 * i - 1):
        print("* ", end="")
        k += 1
    k = 0
    print()
"""
#prog to search the element inside an array
"""
def linearsearch(arr,x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['t','u','t','o','r','i','a','l']
x = 'a'
print(str(linearsearch(arr,x)))
"""
# Queue data structure Implemntation[first in first out]
"""
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def display(self):
        print(self.queue)
    def size(self):
        return len(self.queue)

q= Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
q.dequeue()
print("After removing an element")
q.display()
"""