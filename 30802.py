n = int(input())
size = list(map(int, input().split()))
t,p = map(int, input().split())

a = 0
b = 0
c = 0
for i in size:
    if i%t == 0:
        a += i//t
    else:
        a += (i//t)+1

b = n//p
c = n%p

print(a)
print(b, c)