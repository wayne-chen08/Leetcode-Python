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