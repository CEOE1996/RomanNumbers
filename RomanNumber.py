import re

def ValidNumber(n):
    match = re.search("^M{0,3}(((CM|CD){0,1})|(D{0,1}C{0,3}))(((XC|XL|){0,1})|(L{0,1}X{0,3}))(((IX|IV){0,1})|(V{0,1}I{0,3}))$", n)
    if match: return "True"
    return "False"

print(ValidNumber(input("")))
