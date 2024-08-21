import sys
data = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
data.sort()
for num in data:
    print(num)