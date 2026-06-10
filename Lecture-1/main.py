class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n=len(arr)
        if(n<k):
            return 0
        window_sum = sum(arr[:k])
        max_sum = window_sum
        
        for i in range(k,n):
            window_sum += arr[i] - arr[i-k]
            max_sum = max(max_sum,window_sum)
        return max_sum

# Max Sum Subarray of size K
# Difficulty: EasyAccuracy: 49.6%Submissions: 293K+Points: 2
# Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

# Note: A subarray is a contiguous part of any given array.
