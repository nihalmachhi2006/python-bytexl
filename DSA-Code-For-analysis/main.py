# 3sum
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort array
        result = []
        n = len(nums)

        for i in range(n):

            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            target = -nums[i]

            while left < right:

                current_sum = nums[left] + nums[right]

                if current_sum == target:

                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate values on left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values on right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < target:
                    left += 1

                else:
                    right -= 1

        return result
    


# Squares of a Sorted Array

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
        return res
