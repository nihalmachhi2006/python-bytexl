print('Lecture 8')

# Sq the Array with negative value

# updatea the solution
class Solution:
    # from typing import List
    def sortedSquares(self, nums: List[int]) -> List[int]:
        siz = len(nums)
        neg = []
        pos = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        if len(pos) == 0:
            for x in pos:
                res = x * x
                return res
        if len(neg) == 0:
            for x in neg:
                res = x * x
                return res
        neg = [x*x for x in neg][::-1]
        pos = [x*x for x in pos]
        
        n,m = len(neg),len(pos)
        res = []

        i = j = 0
        while i<n and j<m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1

        while i<n:
            res.append(neg[i])
            i+=1
        while j<m:
            res.append(pos[j])
            j+=1   
        

        
        
        
