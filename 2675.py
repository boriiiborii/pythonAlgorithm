times = int(input())
for _ in range(times):
    num, string = map(str, input().split())
    for i in string:
        print(i*int(num), end="")
    print("")