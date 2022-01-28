import sys
from sys import stdin 

from collections import deque 

N,M = map(int,input().split())



ww = 0
bb = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]
Wqueue = deque()
Bqueue = deque() 

wcnt=1
bcnt=1





mapp=[]
Wvisited=[[False]*N for _ in range(M)] 
Bvisited = [[False]*N for _ in range(M)]


def WBFS():

    while Wqueue:
        curx,cury = Wqueue.popleft()
        
        for i in range(4):
            nx = curx+dx[i]
            ny = cury+dy[i]

            if nx>=0 and nx<M and ny>=0 and ny<N and Wvisited[nx][ny]==False and mapp[nx][ny]=='W':
                Wvisited[nx][ny]=True 
                global wcnt 
                wcnt+=1
                Wqueue.append([nx,ny])


def BBFS():

    while Bqueue:
        curx,cury = Bqueue.popleft()
        
        for i in range(4):
            nx = curx+dx[i]
            ny = cury+dy[i]

            if nx>=0 and nx<M and ny>=0 and ny<N and Bvisited[nx][ny]==False and mapp[nx][ny]=='B':
                Bvisited[nx][ny]=True 
                global bcnt 
                bcnt+=1
                Bqueue.append([nx,ny])





for i in range(M):
    str = stdin.readline()
    inn = []
    for ii in range(len(str)):
        inn.append(str[ii])
    mapp.append(inn)


for x in range(M):
    for y in range(N):
        if mapp[x][y]=='W' and Wvisited[x][y]==False:
            Wqueue.append([x,y])
            Wvisited[x][y]=True
            WBFS()
            ww += (wcnt*wcnt)
            wcnt=1


for x in range(M):
    for y in range(N):
        if mapp[x][y]=='B' and Bvisited[x][y]==False:
            Bqueue.append([x,y])
            Bvisited[x][y]=True
            BBFS()
            bb += (bcnt*bcnt)
            bcnt=1

print(ww,bb)