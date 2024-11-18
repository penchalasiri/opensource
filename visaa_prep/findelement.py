n=int(input())
arr=list(map(int, input().split()))
x=int(input())
def b(arr,x):
    l,h=0,len(arr)-1
    while l<=h:
        m=l+(h-l)
        if arr[m]==x:
            return m
        elif arr[m]<x:
            l=m+1
        else:
            h=m-1
    return -1
print(b(arr,x))
