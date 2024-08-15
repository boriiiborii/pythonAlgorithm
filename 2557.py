numbers = []
for _ in range(9):
    num = int(input())
    numbers.append(num)
maxNum = max(numbers)
print(maxNum)
print(numbers.index(maxNum)+1)