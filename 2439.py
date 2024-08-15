N = int(input())  # 사용자로부터 입력을 받아 N에 저장

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)