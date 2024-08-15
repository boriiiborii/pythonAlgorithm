years = int(input())
if (years%4==0 and not years%100==0) or years%400==0: print(1)
else: print(0)