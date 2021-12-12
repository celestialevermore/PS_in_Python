def solution(N,stages):
    answer=[] 

    totalplayers = len(stages)

    inputdict={
        
    }

    for i in range(N+1):
        tmplist=[]
        inputdict[i].add(tmplist)



    for k,v in enumerate(stages):
        tlist = inputdict[v].values()
        tlist.append(k+1)


    for k,v in inputdict.items():
        print(k,v)



    return answer



tmp = solution(5,[2,1,2,6,2,4,3,3])