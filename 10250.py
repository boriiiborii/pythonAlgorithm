times = int(input())

for _ in range(times):
    a = list(map(int, input().split()))
    hosoo = a[2] // a[0]
    floor = a[2] % a[0]
    if floor != 0:
        hosoo += 1
    else: 
        floor = a[0]
    
    if hosoo < 10:
        print(f"{floor}0{hosoo}")
    else:
        print(f"{floor}{hosoo}")