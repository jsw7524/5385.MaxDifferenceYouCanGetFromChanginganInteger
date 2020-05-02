class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits=str(num)
        maxNum=0
        minNum=999999999
        for i in range(10):
            tmp = digits
            for j in range(10):
                newstr=tmp.replace(str(i),str(j))
                if int(newstr) > maxNum and int(newstr) > 0 and len(str(int(newstr))) == len(digits):
                    maxNum=int(newstr)
                if int(newstr) < minNum and int(newstr) > 0 and len(str(int(newstr))) == len(digits):
                    minNum=int(newstr)
        return maxNum-minNum

sln=Solution()
assert 888==sln.maxDiff(num = 555)
assert 8==sln.maxDiff(num = 9)
assert 820000==sln.maxDiff(num = 123456)
assert 80000==sln.maxDiff(num = 10000)
assert 8700==sln.maxDiff(num = 9288)



