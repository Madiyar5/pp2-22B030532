import re
txt = input()

#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
x = re.search("ab{2,3}", txt )

print(x)