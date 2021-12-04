R,C = map(int,input().split())

dx=[0,1,-1,0]
dy=[1,0,0,-1]


mapp = [[0]*C for _ in range(R)]


def BFS(queue,cnt,visited):
    
    
    #print('currentx :',curx,'currenty :',cury)
    
    while queue:
        curx,cury = queue[0][0],queue[0][1]
        del queue[0] 
        
        for i in range(4):
            nextx,nexty = curx+dx[i],cury+dy[i]
            #print('다음 x :',nextx,'다음 y :',nexty)
            if nextx>=0 and nextx<R and nexty>=0 and nexty<C and mapp[nextx][nexty]!='#' and (nextx,nexty) not in visited:
                # . 이든 o이든 v이든 일단 카운트할 수 있으니까.
                #print("<<<탐색 시작>>>")


                if mapp[nextx][nexty]=='v':
                    #print(nextx,nexty,'에서 늑대 발견')
                    cnt[0]+=1
                    visited.append((nextx,nexty))
                    queue.append((nextx,nexty))
                    #print("queue :", queue[0][0],queue[0][1])

                elif mapp[nextx][nexty]=='o':
                    #print(nextx,nexty, '에서 양 발견')
                    visited.append((nextx,nexty))
                    queue.append((nextx,nexty))
                    cnt[1]+=1
                    #print("queue :",queue[0][0],queue[0][1])
                
                else:
                    
                    #print(nextx,nexty,'에서 길 발견')
                    visited.append((nextx,nexty))
                    queue.append((nextx,nexty))
                    #print("queue :",queue[0][0],queue[0][1])
                    
                       
    # queue를 전부 돌고 난 다음 양과 늑대의 개수 결정
    # cnt[0] : 늑대 cur[1] : 양
    if cnt[0] >= cnt[1]:
        #양을 전부 다 먹음.
        cnt[1]=0
    else:
        cnt[0]=0 

    return cnt[0],cnt[1]



for i in range(R):
    cur = input()

    for ii in range(len(cur)):
        mapp[i][ii]=cur[ii]

# Test 
# for i in range(R):
#     for ii in range(C):
#         print(mapp[i][ii], end=' ')
#     print()

wolvesres,sheepres=0,0
visited=[]

for r in range(R):
    for c in range(C):
        
        if mapp[r][c]=='v' and (r,c) not in visited:
            
            #print(r,c,"늑대 start")
            cnt=[0,0]
            cnt[0]+=1
            queue=[]
            visited.append((r,c))
            queue.append((r,c))
            
            w,s=BFS(queue,cnt,visited)
            wolvesres+=w 
            sheepres+=s


print(sheepres,wolvesres)