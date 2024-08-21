num = int(input())

count = 0
temp = 666

while True:
    if "666" in str(temp):
        count += 1
    if count == num:
        print(temp)
        break
    temp += 1