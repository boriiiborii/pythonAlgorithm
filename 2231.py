num = int(input())

for i in range(1, num+1):
    text = str(i)
    result = i
    for j in text:
        result += int(j)
    if result == num:
        print(i)
        exit()

print(0)