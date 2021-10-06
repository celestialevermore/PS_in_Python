
N = int(input())
arr=[]
for i in range(N):
    inp = input()
    arr.append(inp)


res= []

for i in range(len(arr)):


    #길이가 짝수일 경우
   
    flag=0
    for j in range(len(arr[i])//2):
        if arr[i][j] == arr[i][len(arr[i])-j-1] or ord(arr[i][j])-32 == ord(arr[i][len(arr[i])-j-1]):
                #print(arr[i][j],ord(arr[i][j]),arr[i][len(arr[i])-j-1],ord(arr[i][len(arr[i])-j-1]))
          pass
            
        else:
          flag=1
          res.append("NO")
          break
    if flag==0:
      res.append("YES")

     
    

  

for i in range(len(res)):
    print('#',end='')
    print(i,end=' ')
    print(res[i])