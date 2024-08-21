n = int(input())

result = (n//10)*2
if int(str(n)[-1]) >= 5:
    result += 1
print(result)