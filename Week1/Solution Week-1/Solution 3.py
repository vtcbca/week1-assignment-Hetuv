#Write a python script to enter any number, if it is integer number,
#then check its palindrome or not. Print appropriate message if it is not palindrom.
n=int(input("enter any number:"))
temp=n
s=0 
while n>0:
 r=n%10
 s=s*10+r 
 n=n//10
if s==temp: 
 print(temp,"is Palindram number")
else: 
 print(temp," is not a plaindram number")
