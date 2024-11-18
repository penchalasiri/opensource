X,Y,Z=map(int, input().split())
a=X*Y
b=Z*24*60
if a<=b:
    print("YES")
else:
    print("NO")
