#Write a python script to enter any string, replace vowel with its position number.
s=list(input('Enter a string:'))
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
c=0
for v in s:
    if v in vowels:
        s[c]=c
    c+=1
new=''.join([str(e) for e in s])
print(new)
