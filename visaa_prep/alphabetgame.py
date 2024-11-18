S=input()
v="aeiouAEIOU"
a=0
b=0
for char in S:
    if char.isalpha():
        if char in v:
            a+=1
        else:
            b+=1
print(f"{a},{b}")
