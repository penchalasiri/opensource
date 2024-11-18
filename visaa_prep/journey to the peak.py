N=int(input())
x=list(map(int, input().split()))
a=0
b=0
for u in x:
    a+=u
    b=max(b,a)
print(b)
