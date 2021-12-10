str = input().split('-')

cur = []
s=0

for i in str[0].split('+'):
    s+=int(i)
print(s)

for i in str[1:]:
    for j in i.split('+'):
        s-=int(j)

print(s)