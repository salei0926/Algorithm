class Solution:
    def longestCommonPrefix(self, strs):
        short = strs[0]
        for i in range(len(strs)):
            if len(short) > len(strs[i]):
                short = strs[i]
        j = 1
        while (j <=len(short)):
            for i in range(1, len(strs)):
                if short[:j] != strs[i][:j]:
                    if j==1:
                       print('输入不存在前缀')
                       return 0
                    else:
                        print('前缀为',short[:j-1])
                        return 0
                else:
                    pass
            j+=1
        print('前缀为',short[:j])
        return 0

strs = ['zzzxxx','zzzsz','dx']
solu = Solution()
solu.longestCommonPrefix(strs)