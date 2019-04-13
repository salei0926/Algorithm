class Solusion():
    def roman2integer(self,roman):
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        for i in range(len(roman)):
            if roman[i] in dict:
                ran = dict[roman[i]]
                if i==0:
                   res = ran
                else:
                    if dict[roman[i]]<=dict[roman[i-1]]:
                        res = res+ran
                    else:
                          res = res + dict[roman[i]] - 2*dict[roman[i-1]]
        print(res)

roman = input('put roman:')
solu = Solusion()
solu.roman2integer(roman)