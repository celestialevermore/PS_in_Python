a = [list(map(int,input().split())) for _ in range(9)]

# 열에 대해 검사
realflag=0
for i in range(9):
    check=[]
    flag=0
    for ii in range(9):
        check.append(a[i][ii])

    for iii in range(1,10):
        if iii not in check:
            flag=1
            realflag=1
            break
    if flag==1:
        break
    else:
        pass


# 행에 대해 검사

for i in range(9):
    check=[]
    flag=0
    for ii in range(9):
        check.append(a[ii][i])

    for iii in range(1,10):
        if iii not in check:
            flag=1
            realflag=1
            break 
    if flag==1:
        break 
    else:
        pass 




for i in range(0,9,3):
    for ii in range(0,9,3):
        #print(i, ii)
        #up to this code, setting up the starting point
        check=[]
        flag=0
        for iii in range(i,i+3):
            for iiii in range(ii,ii+3):
                #print(a[iii][iiii], end=' ')
                check.append(a[iii][iiii])
        for j in range(1,10):
            if j not in check:
                flag=1
                realflag=1
                break
        if flag==1:
            break
    if flag==1:
        break


if realflag==1:
    print("NO")
else:
    print("YES")