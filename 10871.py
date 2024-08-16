a, n = map(int, input().split())
data = list(map(int, input().split()))

for i in data:
    if i < n:
        print(i, end=" ")