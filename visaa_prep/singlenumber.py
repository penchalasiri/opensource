N=int(input())
arr=list(map(int,input().split()))
r=0
for n in arr:
    r^=n
print(r)
