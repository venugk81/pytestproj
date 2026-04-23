# 6. Write a function called "count_vowels"
# that takes a string as input and returns the number
# of vowels (a, e, i, o, u) in that string.

def count_vowels(string1):
    vowels = "aeiou"
    count = 0
    for char in string1:
        if char in vowels:
            count += 1

    return count

print(f"vowels count: {count_vowels("abcdefghi")}")
