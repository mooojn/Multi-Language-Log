# Program to find 
# If the given word 
# Is a palindrome

def is_palindrome(word):        # Palindrome is a word that is 
    return word == word[::-1]   # Same even after being reversed

word=input("Enter a word : ")
print(is_palindrome(word))
