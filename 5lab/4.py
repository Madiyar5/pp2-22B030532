import re

txt = input()

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
x = re.findall("[A-Z]_[a-z]+", txt )

print(x)