import sys
from sys import stdin



M,N = map(int,sys.stdin.readline().split())

rescnt=0

#mapp = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]

#mapp = [[0]*N for _ in range(M)]
mapp=[]

for i in range(M):
    mapp.append(list(map(int,sys.stdin.readline().split())))





visited=[]

dx = [1,0,-1,0,-1,-1,1,1]
dy = [0,1,0,-1,-1,1,-1,1]


queue=[]



def BFS(queue,visited,x,y):


    while queue:
        curx,cury = queue[0][0],queue[0][1]
        del queue[0]


        for i in range(len(dx)):
            nextx = curx+dx[i]
            nexty = cury+dy[i]

            if nextx>=1 and nextx<=M and nexty>=1 and nexty<=N and [nextx,nexty] not in visited and mapp[nextx][nexty]==1:
                visited.append([nextx,nexty])
                queue.append([nextx,nexty])
    
                
                
    






for x in range(M):
    for y in range(N):
        if [x,y] not in visited and mapp[x][y]==1:
            visited.append([x,y])
            queue.append([x,y])
            BFS(queue,visited,x,y)
            rescnt+=1

        








print(rescnt)
