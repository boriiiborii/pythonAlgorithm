result = 1

for _ in range(3):
    result *= int(input())

strResult = str(result)
for i in range(10):
    print(strResult.count(str(i)))
    
