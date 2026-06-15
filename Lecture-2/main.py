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
