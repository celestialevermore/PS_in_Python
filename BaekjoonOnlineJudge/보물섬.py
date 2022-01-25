import sys
from sys import stdin 
from collections import deque 

N,M = map(int,sys.stdin.readline().split())


res = -1
dx=[1,-1,0,0]
dy=[0,0,1,-1]

mapp=[]

queue = deque()


visited = [[False]* M for _ in range(N)] 

for i in range(N):
    str = sys.stdin.readline().strip()
    line=[]
    for ii in range(len(str)):
        line.append(str[ii])
    mapp.append(line)
    


def BFS(queue):
    nx,ny,nc = queue[0]
    while queue:
        cx,cy,cc = queue.popleft()
        for i in range(4):
            nx = cx+ dx[i]
            ny = cy+dy[i]
            nc = cc+1
            if nx>=0 and nx<N and ny>=0 and ny<M and visited[nx][ny]==False and mapp[nx][ny]=='L':
                visited[nx][ny]=True
               # print('next : ',nx,ny,nc)
                queue.append([nx,ny,nc])
    
    #print('res :',nc)
    return nc-1






for x in range(N):
    for y in range(M):
        
        if mapp[x][y]=='L':
            #print('<<<start at :',x,y)
            visited[x][y]=True
            queue.append([x,y,0])
            
            candi = BFS(queue)
            res = max(res,candi)

        for i in range(N):
            for ii in range(M):
                visited[i][ii]=False




print(res)