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


153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = -1
        low = 0
        high = len(nums) - 1

        while(low <= high):
            guess = (low + high) // 2
            if(nums[guess] > nums[len(nums) - 1]):
                low =  guess + 1 
            else:
                ans = nums[guess]
                high = guess - 1
        return ans


33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        low = 0
        high = len(nums) - 1

        while(low <= high):
            guess = (low + high) // 2
            if(nums[guess] > nums[len(nums) - 1]):
                if(nums[guess] == target):
                    return guess
                elif(nums[guess] < target):
                    low = guess + 1 
                else:
                    if(nums[0] > target):
                        low = guess + 1
                    else:
                        high = guess - 1
            else:
                if(nums[guess] == target):
                    return guess
                elif(nums[guess] < target):
                    high = guess - 1
                else:
                    if(nums[len(nums) - 1] > target):
                        high = guess - 1
                    else:
                        low = guess + 1
        return ans


# Maximum Sum Subarray of Size K (easy)


# class Solution {
#     public int maxSubarraySum(int[] arr, int k) {
#         int low = 0;
#         int high = k - 1;
#         int ans = 0;
#         int sum = 0;
#         int n = arr.length - 1;

#         for (int i = 0; i <= high; i++) {
#             sum += arr[i];
#         }

#         while (high <= n) {
#             ans = Math.max(ans, sum);

#             low++;
#             high++;

#             if (high > n) {
#                 break;
#             }

#             sum -= arr[low - 1];
#             sum += arr[high];
#         }

#         return ans;
#     }
# }  
        
