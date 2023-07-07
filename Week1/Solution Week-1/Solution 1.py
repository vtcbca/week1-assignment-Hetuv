#PYTHON SCRIPT FOR CHECK THE NUMBER IS PRIME OR NOT
N=int(input('Enter any number:'))
a=1
c=0
while a<=N:
    if(N%a==0):
        c+=1
    a+=1
if(c==2):
    print('yes')
else:
    print('no')
