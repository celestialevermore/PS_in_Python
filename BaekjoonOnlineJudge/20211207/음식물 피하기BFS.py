N,M,K = map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]

mapp =[['.']*M for _ in range(N)]




for i in range(K):
    a,b, = map(int,input().split())
    mapp[a-1][b-1]='#'





queue=[]
visited=[]
cntlist=[0]*1000
index=-1
res=[]
maxi=-1
def BFS(visited,curcnt, queue):


    while queue:
        cx,cy = queue[0][0],queue[0][1]
        del queue[0]

        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]

            if nx>=0 and nx<N and ny >=0 and ny <M and [nx,ny] not in visited and mapp[nx][ny]=='#':
                #print('next :',nx,ny)
                visited.append([nx,ny])
                queue.append([nx,ny])
                curcnt+=1

    return curcnt

    








for x in range(N):
    for y in range(M):
        if mapp[x][y]=='#'and [x,y] not in visited:
            
            visited.append([x,y])
           #print('start at :',x,y)
            index+=1
            cntlist[index]+=1
            queue.append([x,y])
            candi=BFS(visited,cntlist[index],queue)
            cntlist[index]=candi
            #print('cur cntlist[index] :',cntlist[index])

            



print(max(cntlist))