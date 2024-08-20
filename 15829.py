times = int(input())
text = str(input())

count = 0
result = 0
for c in text:
    num = ord(c)-96
    result += num*(31 ** count)
    count += 1

print(result)