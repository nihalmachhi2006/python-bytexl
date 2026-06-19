print('Lecture 2')
Aggressive Cows

You are given an array with unique elements of stalls[], which denote the positions of stalls. You are also given an integer k which denotes the number of aggressive cows. The task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

class Solution:
    def aggressiveCows(self, stalls, k):
        # code here
        
        stalls.sort()   # sorting required
        
        n = len(stalls)
        low = 1
        high = stalls[n - 1] - stalls[0]
        ans = -1
        
        def cheackforspace(stalls, n, k, guess):
            
            cows = 1
            prevpos = stalls[0]
            
            for i in range(1, n):
                
                distance = stalls[i] - prevpos
                
                # place cow if minimum distance condition satisfies
                if(distance >= guess):
                    cows += 1
                    prevpos = stalls[i]
                
                # if k cows placed successfully
                if(cows >= k):
                    return True
            
            return False
        
        while(low <= high):
            
            guess = (low + high) // 2
            
            if cheackforspace(stalls, n, k, guess):
                
                ans = guess
                
                # try for larger minimum distance
                low = guess + 1
                
            else:
                
                # reduce distance
                high = guess - 1
        
        return ans

# Allocate Minimum Pages 

class Solution:
    def findPages(self, arr, k):
        # code here
        n = len(arr)
        students = k

        if n < students:
            return -1

        low = max(arr)
        high = sum(arr)
        ans = -1

        def search(arr, n, limit, students):
            cnt = 1
            pages = 0

            for i in range(n):
                if pages + arr[i] <= limit:
                    pages += arr[i]
                else:
                    cnt += 1
                    pages = arr[i]

                    if cnt > students:
                        return False

            return True

        while low <= high:
            guess = (low + high) // 2

            if search(arr, n, guess, students):
                ans = guess
                high = guess - 1
            else:
                low = guess + 1

        return ans


# fixd windows 
class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        low = 0
        high = k - 1
        sum = 0
        ans = 0
        n = len(arr)
        for i in range(low,high+1):
            sum = sum + arr[i]
            
        while(high<n):
            ans = max(ans,sum)
            low +=1
            high+=1
            if(high == n):
                break
            sum = sum - arr[low - 1]
            sum = sum + arr[high]
        return ans
