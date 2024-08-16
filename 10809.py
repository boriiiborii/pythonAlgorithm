text = input()

for i in range(97,123):
    alpha = chr(i)
    if alpha in text:
        print(text.index(alpha), end="")
    else:
        print("-1", end="")
    print(end=" ")