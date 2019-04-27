class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            if s[i] == ")":
                if stack == [] or stack.pop() != "(":
                    print(False)
                    return False
            if s[i] == "}":
                if stack == [] or stack.pop() != "{":
                    print(False)
                    return False
            if s[i] == "]":
                if stack == [] or stack.pop() != "[":
                    print(False)
                    return False
        if stack:
            print(False)
            return False
        else:
            print(True)
            return True
solu = Solution()
s = '{[]}()}}'
solu.isValid(s)