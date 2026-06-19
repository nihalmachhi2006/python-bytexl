print('Lecture 8')

# Sq the Array with negative value

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
            pos=[]
            neg=[]
            n = len(nums)

            for i in nums:
                if(i<0):
                    neg.append(i)
                else:
                    pos.append(i)
            
            if(len(neg) == 0):
                for x in neg:
                    x * x
                return
            if(len(pos) == 0):
                for x in pos:
                    ans = x*x
                    ans.reverse
                return ans

            neg = [x*x for x in neg][::-1]
            pos = [x*x for x in pos]

            n = len(neg)
            m = len(pos)

            i = 0
            j = 0
            ans = []
            while(i<n and j<m):
                if(neg[i] < pos[j]):
                    ans.append(neg[i])
                    i+=1
                else:
                    ans.append(pos[j])
                    j+=1
            while(i<n):
                ans.append(neg[i])
                i+=1
            while(j<m):
                ans.append(pos[j])
                j+=1
            return ans          
        

        
        
        
