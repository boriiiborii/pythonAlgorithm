times = int(input())

for _ in range(times):
    a = input()
    plusScore = 1
    result = 0
    for i in a:
        if i == "O":
            result += plusScore
            plusScore += 1
        else: plusScore = 1
    print(result)