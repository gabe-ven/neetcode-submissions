# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        res = []
        q = deque([root])
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                val = q.popleft()
                if val:
                    level.append(val.val)
                    q.append(val.left)
                    q.append(val.right)
                
            if level:
                res.append(level)
        
        return res

