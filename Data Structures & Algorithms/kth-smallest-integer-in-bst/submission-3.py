# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # 1. Go left as far as possible.
        # 2. Pop a node = visit it.
        # 3. Count it.
        # 4. Go right.
        # 5. Repeat.
        
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            k -= 1

            if k == 0:
                return curr.val
            
            curr = curr.right
        
    