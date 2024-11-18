N=int(input())
arr=list(map(int,input().split()))
a=True
for i in range(N-1):
    if arr[i]>arr[i+1]:
        a=False
        break
print("true" if a else "false")
