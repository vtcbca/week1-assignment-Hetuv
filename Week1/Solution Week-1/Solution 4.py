#Write a python script to enter any number, if it is integer number,
#then check its armstrong or not. Print appropriate message if it is not armstrong.
s=0 
n=int(input("Enter Your Number: ")) 
temp=n
b=len(str(n))
for i in range(1,b+1): 
 r=n%10
 s=s+(r**b)
 n=n//10 
if temp==s: 
 print("Armstrong Number") 
else: 
 print("Not a Armstorng Number")
