print('Lecture 9')







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# level-oreder tranversal
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = Queue()
        q.put(root)

        ans = []

        while not q.empty():
            level_size = q.qsize()
            level = []

            for _ in range(level_size):
                node = q.get()
                level.append(node.val)

                if node.left:
                    q.put(node.left)

                if node.right:
                    q.put(node.right)

            ans.append(level)

        return ans


# Same Tree

 def fun(p,q):
            if(p == None and q == None):
                return True
            if(p == None or q == None):
                return False
            if(p.val != q.val):
                return False

            r1 = fun(p.left,q.left)
            r2 = fun(p.right,q.right)

            if(r1 == True and r2 == True):
                return True
            return False

        return fun(p,q)



# geeksforgeeks
# Search...
# Courses
# Tutorials
# Practice
# Jobs

# 99+
# N


# Array Subset
# Difficulty: BasicAccuracy: 44.05%Submissions: 573K+Points: 1Average Time: 20m
# Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

# Examples:

# Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
# Output: true
# Explanation: b[] is a subset of a[]
# Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
# Output: true
# Explanation: b[] is a subset of a[]
# Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
# Output: false
# Explanation: b[] is not a subset of a[]
# Constraints:
# 1 <= a.size(), b.size() <= 105
# 1 <= a[i], b[j] <= 106



class Solution {
    public boolean isSubset(int a[], int b[]) {
        // Your code here
      
        Arrays.sort(a);
        Arrays.sort(b);
        for(int i=0 ;i < b.length; i++){
            boolean flag = false;
            for(int j=i ;j < a.length; j++){
                if(b[i] == a[j]){
                    flag = true;
                    break;
                }
            }
            if (!flag){
                return false;
            }
        }
        return true;
    }
}
