h,m = map(int, input().split())
if m >= 45: m -= 45
else: 
    h -= 1
    m += 15

if h == -1 :
    h = 23
print(h, m)