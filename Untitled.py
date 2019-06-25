"""June 25, 2019
number = int(input("give me a number: "))

if number > 0:
    if number % 4 is 0:
        print(number, "is an even number & can be divided by 4")
    elif number % 2 is 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")
"""
"""#3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_2 = []

for i in a:
    if i<5:
        a_2.append(i)

print(a_2)
"""

"""#4
number = int(input("give me a number: "))
divisors = []

for i in range(2,number):
    if number % i is 0:
        divisors.append(i)

print("divisors for your number", number, ": ", divisors)
"""

"""#5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
for i in a:
    for e in b:
        if i == e:
            c.append(i)

c = list(set(c))
print(c)
"""

"""#6
word = input("type in a string: ")
###def reverse(word):
    x = ""
    for i in range(len(word)):
        x += word[len(word)-1-i]
        return x

x = reverse(word)
print(x)
###

word = input("type in a string: ")
x = ""
for i in range(len(word)):
    x += word[len(word)-1-i]
print(x)

if x == word:
    print("this is a palindrome")
else:
    print("this is NOT a palindrome")

wrd = input("type in a string: ")
wrd = str(wrd)
rvs = wrd[::-1]
print(rvs)
if wrd == rvs:
    print("this is a palindrome")
else:
    print("this is NOT a palindrome")
"""

#7
