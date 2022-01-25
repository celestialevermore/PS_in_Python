import sys 
from sys import stdin 
from collections import deque 


n,m = map(int,sys.stdin.readline().split())

visited=[[False]*1001 for _ in range(1001)]

mapp = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

queue = deque()

dx=[1,0,-1,0]
dy=[0,1,0,-1]


def BFS(queue):

    while queue:
        curx,cury,curz = queue.popleft()
        #print(curx,cury,curz)
        for i in range(4):
            nextx = curx+dx[i]
            nexty = cury+dy[i]
            nextz = curz+1
            if nextx >=0 and nextx<n and nexty>=0 and nexty<m and visited[nextx][nexty]==False and mapp[nextx][nexty]!=0:
                
                visited[nextx][nexty]=True 
                mapp[nextx][nexty]=nextz
                #print('x y z',nextx,nexty,nextz)
                
                queue.append([nextx,nexty,nextz])





for i in range(n):
    for ii in range(m):
        if mapp[i][ii]==2 and visited[i][ii]==False:
            
            mapp[i][ii]=0
            queue.append([i,ii,mapp[i][ii]])
            visited[i][ii]=True            
            BFS(queue)

for i in range(n):
    for ii in range(m):
        if visited[i][ii]==False and mapp[i][ii]!=0:
            mapp[i][ii]=-1


for i in range(n):
    for ii in range(m):
        print(mapp[i][ii],end=' ')
    print()

