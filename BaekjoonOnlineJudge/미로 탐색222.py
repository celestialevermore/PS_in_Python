import sys
from sys import stdin 
from collections import deque 

N,M = map(int,input().split())

mapp=[]
visited=[[False]*M for _ in range(N)]

dx = [1,-1,0,0]

dy = [0,0,1,-1]
res = 100000

def BFS(queue):

    while queue:
        curx,cury,curc = queue.popleft()
        
        if curx==N-1 and cury == M-1:
            visited[curx][cury]=True 
            global res
            if res>=curc:
                res= curc 




        for i in range(4):
            nx = curx+dx[i]
            ny = cury+dy[i]
            nc = curc+1

            if nx>=0 and nx<N and ny>=0 and ny<M and visited[nx][ny]==False and mapp[nx][ny]=='1':
                visited[nx][ny]=True 
                next = [nx,ny,nc]
                queue.append(next)






for i in range(N):
    str = sys.stdin.readline().strip()
    inputs=[]
    for x in range(len(str)):
        inputs.append(str[x])
    mapp.append(inputs)



start = [0,0,1]
queue = deque()

queue.append(start)


BFS(queue)

print(res)
