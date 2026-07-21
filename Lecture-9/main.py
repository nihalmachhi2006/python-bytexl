print('Lecture 9')



# what is CSS Grid

# CSS grid is a two dimensional layout model that arrange
# items in rows and columns

# Grid has to main components
# 1. Grid Container (Parent)
# 2. Grid Items  (Direct Children)

# Grid also have two axis
# 1. columns axis (y)
# 2. row axis (x)

# *Grid is divided into  grid cells by grid lines

# * Grid Lines defines grid tracks (Rows and Columns)
# * Grid Columns and Rows have SPACING between them called grid lines


# we've covered display Properties
# {
#   display : ?
# }

# 1.Block
# 2.Inline
# 3.Inline-block
# 4.Flex
# 5.Grid
# 6.


# Grid Container Properties
# 1. Grid Template Column and Rows
# 2. Fractional Unit
# 3. Repeat Function


# Note: Grid Items will display in single column by default
# display: grid



# Property

# 1. Grid Template Column:  Defines the NUMBER OF Columns and Width

# grid-template-column: 200px 100px 300px

# No. of columns : 3

# 2. Grid Template Rows : Sets the number of rows and height of each
# grid-template-rows: 200px




# =========== 4-6-2026 =============

# grid-template-column :  200px 100px auto;
# grid-template-columns: 1fr 2fr 1fr;
# grid-template-rows: 1fr 2fr 1fr;
# grid-template-columns: repeat(3, 300px);
# grid-template-columns: repeat(auto-fill, 200px);
# auto-fill :  add extra columns when space available

# grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
# Fit the columns based on the minmax() func.
# auto-fit: fits the cells into width



# grid-auto-columns: 300px;
# grid-auto-flow: column;
# overflow-x: scroll;


# Website 1:  https://curioos.giantart.com/?_ab=0&_fd=0&_sc=1&pb=0
# Website 2 : https://www.grundini.com/


# https://chromewebstore.google.com/detail/colorzilla/bhlhnicpbhignbdhedgjhgdocnmhomnp
# https://chromewebstore.google.com/detail/download-all-images/nnffbdeachhbpfapjklmpnmjcgamcdmm
# https://chromewebstore.google.com/detail/fonts-ninja/eljapbgkmlngdpckoiiibecpemleclhh



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
 # transpost

# class Solution {
#     public int[][] transpose(int[][] matrix) {
#     int n = matrix[0].length;
#     int m = matrix.length;
#     int ans[][] = new int[n][m];
   
#     for(int i = 0; i<matrix[0].length; i++){
#         for(int j = 0; j<matrix.length; j++){
#             ans[i][j] = matrix[j][i];
#         }
#      } 
#      return ans;  
#     }
# }
