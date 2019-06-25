"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""

word = input("type in a string: ")
def reverse(word):
    x = ""
    for i in range(len(word)):
        x += word[len(word)-1-i]
        return x

x = reverse(word)
print(x)
"""
x COMES BACK WITH ONLY THE LAST LETTER AND DOESN'T LOOP
"""

word = input("type in a string: ")


if x == word:
    print("this is a palindrome")
else:
    print("this is NOT a palindrome")

    
""" IF I DON'T DO DEF, IT WORKS FINE, LIKE BELOW:
x = ""
for i in range(len(word)):
    x += word[len(word)-1-i]
print(x)
"""
