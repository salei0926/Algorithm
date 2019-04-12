class PalindromeNumber():
    def determine(self,integer):
        integer = str(integer)
        for i in range(int(len(integer)/2)):
            if integer[i]!=integer[-1-i]:
                print(False)
                return False
            print(True)
            return True
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x%10==0 and x>0:
            return False
        right = 0
        while x>right:
            right = right*10+x%10
            x=x//10
        if x==right or x==right//10:
            return True
        else:
            return False
integer = input('请输入数字：')
palin = PalindromeNumber()
palin.determine(integer)