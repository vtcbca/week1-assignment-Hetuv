#Write a python script to enter any string and count vowel.
string=input('Enter a string:')
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowelCount = 0
for v in string:
    if v in vowels:
        vowelCount += 1
print("The string contains", vowelCount, "vowels in it")
