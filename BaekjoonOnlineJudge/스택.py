N = int(input())



stack=[]
res=[]
for i in range(N):
    order = input().split(' ')
    
    if order[0]=='push':
        stack.append(int(order[1]))
    elif order[0]=='top':
        if stack:
            
            res.append(stack[-1])
        else:
            
            res.append(-1)
    elif order[0]=='size':
        
        res.append(len(stack))
    elif order[0]=='pop':
        if stack:
            
            res.append(stack[-1])
            stack.pop()
        else:
            
            res.append(-1)
    elif order[0]=='empty':
        if len(stack)==0:
            
            res.append(1)
        else:
            
            res.append(0)


for i in range(len(res)):
    print(res[i])




