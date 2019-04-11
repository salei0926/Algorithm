start = input('please put in number and strings')
start = start.split(' ')
res=[]
strs=[]
def splitstr(stri):
    strs=[]
    while len(stri)>8:
        strs.append(stri[0:8])
        stri = stri[8:]
    strs.append(stri+'0'*(8-len(stri)))
    print(strs)
    return strs
for i in start[1:]:

    if len(i)==8:
        res.append(i)
    elif len(i)<8:
        res.append(i+'0'*(8-len(i)))
    else:
        for s in splitstr(i):
           print('iiiii',i)
           res.append(s)
print(res)