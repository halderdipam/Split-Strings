
def solution(s):
    l=[]
    for i in range(0,len(s),2):
        l.append(s[i:i+2])
    if len(s)%2 !=0:
        l[-1] = l[-1]+'_'
        return l
    else: return l
