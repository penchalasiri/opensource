X=int(input().strip())
d1 = 0.1*X
d2=100
max_discount=max(d1,d2)
f = X-max_discount
print(int(f))
