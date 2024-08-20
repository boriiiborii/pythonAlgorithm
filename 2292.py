num = int(input())

if num == 1: 
    print(1)
    exit()

i = 1
count = 1

while(True):
    i += 6 * count
    count += 1
    
    if num <= i:
        print(count)
        break