def solution(new_id):
    cur=  ""
    #1단계
    for i in range(len(new_id)):
        if new_id[i].isupper():
            cur+=new_id[i].lower()
        else:
            cur+=new_id[i]


    #2단계
    curn=""
    for i in range(len(cur)):
        if cur[i]=='_' or cur[i] =='-' or cur[i].islower() or cur[i]=='.' or cur[i].isnumeric():
            curn+=cur[i]

    cur = curn
   

    #3단계
    curn=" "
    for i in range(len(cur)):
        if cur[i]=='.' and curn[-1]=='.':
            pass 
        else:
            curn+=cur[i]

    cur=curn[1:]
    #print(cur[0])

    #4단계
    curn=''
    if cur[0]=='.' and cur[-1]!='.':
        curn = cur[1:]
    elif cur[0]=='.' and cur[-1]=='.':
        curn = cur[1:-1]
    elif cur[0]!='.' and cur[-1]=='.':
        curn = cur[:-1]
    else:
        curn=cur

    cur = curn 

   # print('5 :',cur)
    #5단계
    if len(cur)==0:
        cur+='a'

    
    #6단계
    curn=""
    index=0
    if len(cur)>=16:
        while len(curn)<15:
            curn+=cur[index]
            index+=1
        if curn[-1]=='.':
            cur = curn[:-1]
        else:
            cur=curn




   # print(cur)
    #7단계
    curn=""
    if len(cur)==1:
        cur+=cur[-1]
        cur+=cur[-1]
    elif len(cur)==2:
        cur+=cur[-1]

    

    return cur

    



test = solution("abcdefghijklmn.p")
print(test)
        