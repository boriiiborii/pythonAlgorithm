array = [[1] * 16 for _ in range(16)]
for i in range(1, 16):
    for j in range(1, 16):
        if j == 0:
            continue
        
        array[i][j] = array[i-1][j]+array[i][j-1]

for _ in range(int(input())):
    for _ in range(2):
        n = int(input())
        m = int(input())
        print(array[n][m-1])
