from sys import stdin

N = int(stdin.readline())

pat = stdin.readline().rstrip()

s=""
e=""
idx=0
res=[]
for i in range(len(pat)):
    if pat[i]=='*':
        idx=i
        break 
s = pat[:idx]
e = pat[idx+1:]


for i in range(N):
    string = input()
    ss = string.find(s)
    #print('e:', e,'endline :',string[len(string)-len(e):])
    if string[len(string)-len(e):] == e and string[:len(s)]==s and len(s)+len(e)<=len(string):
        res.append("DA")
    else:
        res.append("NE")


for i in range(len(res)):
    print(res[i])