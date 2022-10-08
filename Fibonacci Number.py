
# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
#[using Recursion]

def rec(n):
    if n<=1:
        return n
    else:
        return (rec(n-1)+rec(n-2))
nterm=int(input("Enter any Number - "))
if nterm<=0:
    print("Please Enter a positive a Integer")
else:
    print("Fibonacci Series")
    for i in range(nterm):
        print(rec(i),end=" ")

#[using Iteration]

num=int(input("Enter the Numbr to which you wanted the series - "))
nth=0
n1,n2=0,1
count=0
if num<=0:
    print("enter a positive num")
elif num==1:
    print(n1)
else:
    while count < num:
        print(n1,end=" ")
        #Updating Values
        nth=n1+n2
        n1=n2
        n2=nth
        count += 1
