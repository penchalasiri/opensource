Z=int(input())
if (Z%4==0 and (Z%100!=0 or Z %400==0)):
    print("YES")
else:
    print("NO")
