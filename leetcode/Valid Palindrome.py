'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

s = "A man, a plan, a canal: Panama"

boo = False
result = ""
for i in range(len(s)):
    if s[i].isalpha() or s[i].isdigit():
        result += s[i]

result = result.lower()

reverse = result[::-1]

if result == reverse:
    boo = True

print(result)
print(reverse)
print(boo)
