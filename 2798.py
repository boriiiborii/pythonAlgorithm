from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

resultSum = 0

combi = list(combinations(data, 3))

for i in combi:
    currentSum = sum(i)
    if resultSum < currentSum and m >= currentSum:
        resultSum = currentSum

print(resultSum)

