N = int(input())


dx = [0,1,-1,0]
dy=[1,0,0,-1]






mapp=[[0]*N for _ in range(N)]
visited=[]


def BFS(mapp,queue,visited):

    while queue:
        curx,cury = queue[0][0],queue[0][1]
        del queue[0]

        for i in range(4):
            nextx,nexty = curx+dx[i],cury+dy[i]

            if nextx>=0 and nextx<N and nexty>=0 and nexty<N and [nextx,nexty] not in visited:
                visited.append([nextx,nexty])
                queue.append([nextx,nexty])

    return 1 



for i in range(N):
    string = list(map(int,input().split()))

    for ii in range(len(string)):
        mapp[i][ii]=string[ii]




maxheight =0 
for i in range(N):
    for ii in range(N):
        if maxheight <=mapp[i][ii]:
            maxheight=mapp[i][ii]



maxx=-1



for i in range(maxheight):
    #높이가 0 ~ maxheight 사이로 주어짐
    height = i 
    visited=[]
    queue=[]
    #방문 표시를 먼저 전부 해준다.
    for x in range(N):
        for y in range(N):
            if height >= mapp[x][y]:
                visited.append([x,y])

    #영역의 갯수
    cur=0
    for x in range(N):
        for y in range(N):
            if [x,y] not in visited:
                visited.append([x,y])
                queue.append([x,y])
                cur+=BFS(mapp,queue,visited)
    



    if maxx <=cur:
        maxx = cur



print(maxx)