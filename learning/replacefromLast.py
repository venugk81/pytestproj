
text = "one two three two one"
sub = "two"
replacement = "LAST"

index = text.rfind(sub) #14
if index != -1:
    result = text[:index] + replacement + text[index + len(sub):]
             #one two three  +   sub +  one (14+3=17)
else:
    result = text

print(result)


text = "one two three two one"
result = "LAST".join(text.rsplit("two", 1))
        #['one two three ', ' one']
print(result)
# When to use which?
# Use rsplit() → simpler and cleaner
# Use rfind() → more control (e.g., conditional logic)

j= "join"
a = ['a ', ' b ', ' c ']

print(j.join(a))

import re

def is_valid_website(url):
    pattern = r'^(http|https?:\/\/)?(www\.)?\w+\.\D{2,}?$'
    return bool(re.match(pattern, url))

website = input("Enter a website name: ")

if is_valid_website(website):
    print(True)
else:
    print(False)

"""

Syntax of String Slicing in Python
substring = s[start : end : step]

Parameters:

s: The original string.
start (optional): Starting index (inclusive). Defaults to 0 if omitted.
end (optional): Stopping index (exclusive). Defaults to the end of the string if omitted.
step (optional): Interval between indices. A positive value slices from left to right, while a negative value slices from right to left. If omitted, it defaults to 1 (no skipping of characters).


s[-4:] slices the string starting from the 4th character from the end ('m') to the end of the string.
s[:-3] slices the string from the beginning up to the 3rd character from the end ('k'), excluding it.
s[-5:-2] slices the string from the 5th character from the end ('l') to the 2nd character from the end
 ('n'), excluding the last character.
s[-8:-1:2] slices the string from the 8th character from the end ('g') to the 2nd character from the 
    end ('n'), with a step of 2, taking every second character.
    
    reverse a string: print(s[::-1])
    
    gets all string chars
    s = "Hello, World!"

# Get the entire string
s2 = s[:]
s3 = s[::]

# Characters from index 7 to the end
print(s[7:])

# Characters from the start up to index 5 (exclusive)
print(s[:5])

s = "abcdefghi"

# Every second character
print(s[::2])

# Every third character from index 1 to 8 (exclusive)
print(s[1:8:3]) 
    
"""

print(7//2)