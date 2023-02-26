import re

txt = input()

#Write a python program to convert snake case string to camel case string.
m = txt.split('_')
text = ''
for i in range(len(m)):
    x = m[i].capitalize()
    text += x

print(text)