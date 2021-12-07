stringa = input()

curset = set()


for i in range(len(stringa)):
    curset.add(stringa[i])

print(curset)



def solution(s):

    for curlen in range(len(s)):
        curset = set()

        #단위만큼 집합에 추가
        for i in range(len(s),curlen):
            curvoc =""
            curvoc+=s[i]
            curset.add(curvoc)
        
