
N = int(input())
res=[]


arr = input().split()


def digit_sum(x):
    total=int(0)

    for i in range(len(x)):
        total+=int(x[i])
    return total


for i in arr:
    res.append(digit_sum(i))

curmax=-1

for i in range(len(res)):
    if curmax <=res[i]:
        curmax = res[i]

Key=0
for key,value in enumerate(res):
    if curmax == value:
        Key=key
        break

print(arr[Key])