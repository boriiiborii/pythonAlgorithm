n = int(input())
text = [str(input()) for i in range(n)]

word = list(set(text))
word.sort()
word.sort(key=len)

for i in word:
    print(i)