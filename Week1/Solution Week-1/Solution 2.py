#Write a python script to enter any number and print the sum of its digit.
a=int(input("enter any number:"))
n=a
b=0
c=0
x=0
while a>0:
    c=a%10
    b=b+c
    a=a//10
    x+=1
s=str(n)
output=map(int,s)
print("sum of",list(output),'=',b)

