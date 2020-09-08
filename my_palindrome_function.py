# Task: Check if the user entered string is a palindrome or not
# Palindrome: A palindrome is a word or phrase that reads the same forwards as it does backwards e.g level
# Input: string which is to be evaluated
# Output: Boolean output showing True or False
# Note: Function should only consider letters
#     : Ignore upper and lower case

b: str = input("Enter a string: ")

def is_a_palindrome(a):
    a1 = a.lower() # Lowers all the values of the string
    a1 = ''.join(filter(str.isalpha, a1))
    a2 = "" # Empty string initialization
    for i in a1[::-1]:
        a2 += i # adds the reversed alphabets in this variable
    if  a1 == a2 :
        print("True")
    else:
        print("False")

is_a_palindrome(b)



