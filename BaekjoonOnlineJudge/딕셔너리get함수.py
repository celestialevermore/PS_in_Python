genres = ["classic","pop","classic","classic","pop"]

plays = [500,600,150,800,2500]

playDic={}

dic={}

for i in range(len(genres)):
    playDic[genres[i]]=playDic.get(genres[i],0)+plays[i]

    dic[genres[i]]=dic.get(genres[i],[])+[(plays[i],i)]

print(playDic)
print(dic)