import re 

txt = input()

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
x = re.sub("[ ,.]", ":", txt)

print(x)