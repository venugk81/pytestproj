# Valid Identifiers
import re

my_variable = 25
counter = 40.7
_total = "Hello"
Name123 = 136
myFunction = True
_data = False

#Invalid Identifiers
# 123abc = 34     #cant start with numbers
# my variable =6.7        #cant have space
# @count = "hi"       @special char
# for = "True"    for is a python keyword
# if_condition? = "Innomatics"    ? not allowed
# class = "Hyderabad"     class is a python keyword

# ==============2==============

_int_value = 10
_int_negative_value = -5
_pi = 3.14159
_dec_value = -0.12345
_int_k = 1000
_str_hello = "Hello, World!"
_str_py = "Python"
_str_learning = "I am learning"
_str_type = "Text type"
_str = "String"
a = True
_bool_false = False

# ===========3=======
s = "$python is fun, python is easy, but python is tough when you don't practice it revise it@ "
print("number of characters in a string: ", len(s))
arr_spl = s.split(",")
print(arr_spl)
# 3.
print("3. Count the frequency of 'python': ", s.count("python"))
# 4
print("4. Count the frequency of 'is': ", s.count("is"))

print("check the +,-,*,/,// of 3 and 4 results")
_python_cnt = s.count("python")
_is_cnt = s.count("is")

print("python_cnt + _is_cnt: ", _python_cnt + _is_cnt)  #7
print("python_cnt - _is_cnt: ", _python_cnt - _is_cnt)  #-1
print("python_cnt * _is_cnt: ", _python_cnt * _is_cnt)  #12
print("python_cnt / _is_cnt: ", _python_cnt / _is_cnt)  #0.75
print("python_cnt % _is_cnt: ", _python_cnt % _is_cnt)  #3
print("python_cnt // _is_cnt: ", _python_cnt // _is_cnt)  #0

# replace "when " with "if and only if"
s1 = s.replace("when", "if and only if")
print(s1)  #$python is fun, python is easy, but python is tough if and only if you don't practice it revise it@

"""
7. find the difference between the number of characters in the original 
string and the number of characters when you replace 
"python " with "data science". replace 
 only the last occurring python with data sciences
 """

lst_python = s.rsplit("python", 1)
new_str = "data science".join(lst_python)
print(new_str)
#$python is fun, python is easy, but data science is tough when you don't practice it revise it@

# 8. read a string dynamically (user input)
# if your string is having odd number of characters print:
# true otherwise print : False eg: Innomatics
# : o/p : False, datascience : o/p : True

txt_user_input = input("\n8. Enter any string to check if string length is odd or ever: ")
str_len = len(txt_user_input)
if str_len % 2 == 0:
    print("String is even: ", True)
else:
    print("String is odd: ", False)

# 9. Ask user to enter a website name and check whether it is valid or not(True/False)
# http://doman.com
# https://discord.com
# https://www.discord.com

def is_valid_website(url):
    pattern = r'^(http|https?:\/\/)?(www\.)?\w+\.\D{2,}?$'
    return bool(re.match(pattern, url))
# website = input("Enter a website name: ")
website = "https://discord.com"

if is_valid_website(website):
    print(True)
else:
    print(False)

#####-------------------------------

# 10 Create a string containing a sentence that includes both single and double quotes.
# Use escape characters to include quotes within the string.
# Print the modified string.

str_quotes = "10. Here is a string \"containing both single\' and double\" quotes"
print(str_quotes)

print("\n")

# 11. Declare a string with a backslash \ character in it.
# Demonstrate the use of the escape character to print the backslash itself.
# Print the resulting string.

str_backslash="11. Here is the string with backslash \\ Demonstrate the use of the escape character"
print(str_backslash)
print("\n")
# 12 . Construct a string containing newline and tab escape sequences.
# Print the string to display the formatted output.

str_esc= "12. Printing next part of string in next line \ncontaining newline and tab\tescape sequences."
print(str_esc)
print("\n")
sentence = "I want to become a Data Scientist"
print("\n13 program.. ")
# Access and print the first character of the string using indexing.
# Access and print the last character of the string using negative indexing.
# What are possible ways to extract Scientist(use forward and reverse)
# Use slicing to extract and print the first word from the string.
# Use slicing to extract and print the last three characters of the string.
print("First Character: ", sentence[0])
print("last Character: ", sentence[-1])
# What are possible ways to extract Scientist(use forward and reverse)
spl_sentence = sentence.split(" ")
print("extract scientist: ", spl_sentence[-1])
print("extract scientist: ", spl_sentence[len(spl_sentence)-1])
print("first word: ", spl_sentence[0])
print("last 3 characters of the string: ", sentence[-3:])

print("\n")

# 14.
# name = "Innomatics Reserach Labs"
# Apply slicing to extract a substring that includes the second to fifth characters.
# Print the extracted substring.

name = "Innomatics Reserach Labs"   ##2nd char: n and 5th char: m
print("14. second to 5th character: ", name[1:5])
print("\n")

# 15.string = "Python@1234"
# Use slicing to extract every second character from the string.
# Print the resulting sliced string.
# print last five letters.
# Utilize slicing to reverse the word order in the string.
# Print the string with the words in the reversed order.

string1 = "Python@1234"
# substring = s[start : end : step]
print("Every second character of the string starting from 1st index: ", string1[1:: 2])
# or
print("Every second character starting from 0th index: ", string1[::2])
print("\n16 Prob")

a = "123123123"
# Apply slicing to extract only the numeric characters at odd positions.
# Print the sliced result.
print("slicing to extract only the numeric characters at odd positions: ", a[::2])

print("\n+++++++++++++++17 problem++++++++:")
name = "Innomatics"
course = "Data Science"
# write python code in different ways to show output as : "Hello World I am learning Data Science in Innomatics"
# Replace Science with Analysis in the above output.
str1 = "Hello World I am learning "+ course+ "in "+ name
print(str1)
print("replace Science with Analysis: ", str1.replace("Science", "Analysis"))

"""string = ' Hello World I am learning Python in Innomatics ' 
How many characters are there in the string?
Slice only 'Python' from above string 
Remove white spaces on both sides then find no.of characters in the string. 
Convert the string in Upper case
What is the index number of 'World' in the above string.
Split the string with respect to whitespace.after that store that split into a variable and find the data type of that variable.
How many times 'a' is repeated in the above string.
"""

print("\n_____________18 problem____________")
str1 = ' Hello World I am learning Python in Innomatics '
print("number of characters in the string: ", len(str1))
ind = str1.find("Python")
print("index of Python: ", ind)

len_python = len("Python")
print("\nSlicing only python: ", str1[ind:ind+len_python])
print("trim the string and count chars length: ", len(str1.strip()))
print("\nUpcase:", str1.upper())
print("index of the World: ", str1.find("World"))

print("\nSplit the string with respect to whitespace.after that store that split into a variable and find the data type of th")
for each in str1.split():
    print(each, "- and its type- ", type(each))

print("\nHow many times 'a' is repeated in the above string.: ", str1.count("a"))

# Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index

print("\n 19 prob--------------")
s ="Earth revolves around the sun"
i = s.find("revolves")
j = s.rfind("sun")
print("\nindex of revolves: ", i, " slicing revolves word: ", s[i: i+len("revolves")])
# s[-3:] slices the string starting from the 3rd character from the end to the end of the string.
print("\nindex of sun: ", j,  "slicing sun word: ", s[j-len(s): ])


"""Create two variables to store how many fruits and vegetables you eat in a day.
Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
"""

str1 = "how many fruits and vegetables you eat in a day."
str2 = "I eat x veggies and y fruits daily"
str3_veg = 2
str3_fruit = 3
print(str2.replace("x", str(str3_veg),1).replace("y", str(str3_fruit),1))

"""
Create 3 variables to store street, city and country, now create address variable to
store the entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line.
"""
street = "Street 1, Tarnaka"
city= "Hyderabad"
country = "Bharat"
Address = "Street: "+ street + " City: " + city + " Country: " + country
print(Address)
Address1 = f"Street: {street} City: {city} Country: {country}"
print(Address1)

