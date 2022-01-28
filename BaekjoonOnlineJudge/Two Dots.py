
import sys 
from sys import stdin 

N,M = map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]

mapp=[]
visited=[[False]*M for _ in range(N)]
alphas=[]
res=[]

for i in range(N):
    str = sys.stdin.readline()

    inputs=[]
    for i in range(len(str)):
        inputs.append(str[i])
    mapp.append(inputs)


for i in range(N):
    for ii in range(M):
        if mapp[i][ii] not in alphas:
            alphas.append(mapp[i][ii])
        else:
            continue






def DFS(start,point,vvisited):

    #print('current :',start[0],start[1],start[2])
    

    for i in range(4):
        nx = start[0]+dx[i]
        ny = start[1]+dy[i]
       #print('nx,ny :',nx,ny)
       

        if nx>=0 and nx<N and ny>=0 and ny<M and visited[nx][ny]==False and mapp[nx][ny]==start[2] and [nx,ny] not in vvisited:
            visited[nx][ny]=True 
            vvisited.append([nx,ny])
            print('next DFS :',nx,ny,mapp[nx][ny])
            DFS([nx,ny,mapp[nx][ny]],point,vvisited)


for i in alphas:
    cur = i
    sx,sy=0,0
    vvisited=[]

    for x in range(N):
        for y in range(M):
            if mapp[x][y]==cur and visited[x][y]==False:
                visited[x][y]=True
               
               
                sx,sy = x,y
                start = [x,y,mapp[x][y]]
                point = [sx,sy]
                DFS(start,point,vvisited)

    if [sx,sy] in vvisited and len(vvisited)>=4:
        res.append('Yes')
    else:
        res.append('No')
    
    print(res)
    



print(res)