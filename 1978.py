_ = int(input())
data = list(map(int, input().split()))
count = 0

for num in data:
    if num == 1: continue
    elif num == 2: 
        count += 1
        continue
    for i in range(2, num):
        if num % i == 0:
            break 
        if i == num-1:
            count += 1

print(count)