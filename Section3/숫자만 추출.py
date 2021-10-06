arr = input()
a=''

for i in range(len(arr)):
    if arr[i].isdigit():
        if len(a)==0 and arr[i]=="0":
            pass
        if len(a)==0 and arr[i]!="0":
            a+=arr[i]
        else:
            a+=arr[i]



res=''
for i in range(len(a)):
    if a[i]=='0':
        pass
    else:
        res+=a[i]

res = int(res)
print(res)

cnt=0
for i in range(1,res+1):
    if res%i==0:
        cnt+=1

print(cnt)