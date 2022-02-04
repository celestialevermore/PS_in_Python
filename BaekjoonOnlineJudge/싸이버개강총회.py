import sys 
from sys import stdin 

S,E,Q = input().split()
print(S,E,Q)
dd = dict()

startset=set()
endset=set()


while True:

    inputs = sys.stdin.readline()
    if len(inputs)<5:
        break
    else:
        inputs = inputs.split()
        time = inputs[0]
        name = inputs[1]
        if time not in dd:
            ddset=set()
            
            dd[time]=ddset
            dd[time].add(name)
        else:
            dd[time].add(name)




dd_time_keys = list(dd.keys())
dd_name_values=list(dd.values())


#print(dd_time_keys)
#print(dd_name_values)

for i in range(len(dd_time_keys)):

    if dd_time_keys[i]<=S:
       # print(dd_time_keys[i],'<',S)
        L = list(dd[dd_time_keys[i]])
        for ii in range(len(L)):
            startset.add(L[ii])

    elif dd_time_keys[i]>=E and dd_time_keys[i]<=Q:
        #print('E <=',dd_time_keys[i],'<=Q')
        L = list(dd[dd_time_keys[i]])
        for ii in range(len(L)):
            endset.add(L[ii])



print(len(startset.intersection(endset)))