class ReverseInteger():
    def reverse(self,integer):
        strd = str(integer)
        if strd[0]=='-':
            strd=strd[1:]
            strd = '-'+strd[::-1]
        elif strd[-1]=='0':
            strd = strd[:-1]
            strd = strd[::-1]
        else:
            strd=strd[::-1]
        print(int(strd))
inter = input('请输入整数')
resv = ReverseInteger()
resv.reverse(inter)
