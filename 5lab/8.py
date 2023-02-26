import re

txt = input()

#Write a Python program to split a string at uppercase letters.
x = re.findall('[A-Z][^A-Z]*', txt)

print(x)