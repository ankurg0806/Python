# Matching Brackets
# Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verify that any and all pairs are matched and nested correctly.


def is_paired(input_string):
    mydict = {']':'[','}':'{',')':'('}
    stack = []
    for char in input_string:
        if char in mydict.values():
            stack.append(char)
        elif char in mydict.keys():
            if not stack or stack.pop() != mydict[char]:
                return False
    return not stack

print(is_paired("(((185 + 223.85) * 15) - 543)/2"))