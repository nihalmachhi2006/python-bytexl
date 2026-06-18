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
