import re

txt = input()

#Write a Python program to insert spaces between words starting with capital letters.
x = re.findall('[A-Z][^A-Z]*', txt)
text = ' '.join(x)

print(text)