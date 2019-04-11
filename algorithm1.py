strd = 'qqq2(e)oo3(b)aa2(n)'
res = []
i = 0
j=0
list_for=[]  #找到前括号下标
list_sub=[]  #找到后括号下标
content=[]   #数字即括号里面的内容
#此循环找到所有括号
for a in strd:
    if a=='(':
        list_for.append(i)
    if a==')':
        list_sub.append(i)
    i+=1
#次循环找到所有数字括号（即被替换的部分），以及新的部分
for j in range(len(list_sub)):
    content.append(strd[list_for[j]-1:list_sub[j]+1])
    res.append(int(strd[list_for[j]-1])*strd[list_for[j]+1:list_sub[j]])
#把所有新内容替换旧内容
for i in range(len(content)):
    strd = strd.replace(content[i],res[i])
#逆序输出
print(strd[::-1])









