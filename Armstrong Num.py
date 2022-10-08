# Python program to check if the number is an Armstrong number or not
# if [1*1*1 + 5*5*5 + 3*3*3 = 153] so 153 is Armstrong

num =int(input("enter the number you wanted to cheak - "))
sum=0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num==sum:
    print("given number is a Armstrong",num,"==",sum)
else:
    print("num is not a Armstrong no",num,"!=",sum)

