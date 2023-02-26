import re

txt = input()

#Write a Python program to convert a given camel case string to snake case.
m = re.findall('[A-Z][^A-Z]*', txt)
for i in range(len(m)):
    m[i] = m[i].lower()

text = '_'.join(m)

print(text)