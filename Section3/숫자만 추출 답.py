s = input()

res=0

for x in s:
    if x.isdecimal():
        res = res*10 + int(x)
print(res)
