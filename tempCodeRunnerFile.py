times = int(input())
for _ in range(times):
    num, string = map(str, input().split())
    print(string*int(num))