'''tow sum'''
class Solution():

    def searchNum(self,num,target):
        dict={}
        for i in range(len(num)):
            x = target - num[i]
            if x  in dict:
                print(dict[x],i)
                return dict[x],i
            dict[num[i]]=i
num = [2,7,11,15]
target = 9
solution = Solution()
solution.searchNum(num,target)