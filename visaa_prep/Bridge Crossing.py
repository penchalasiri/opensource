input_line=input()
X,Y,Z= map(int, input_line.split())
a=Z-Y
if a<0:
    print(0)
else:
    max_mangoes=a//X
    print(max_mangoes)
