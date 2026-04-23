# 4. Write a function called "is_even" that takes an integer as input and returns True if the number is even, and False otherwise.

def check_odd_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

val = int(input("Enter a number to check if its even or odd: "))
if check_odd_even(val):
    print("Even")
else:
    print("Odd")
