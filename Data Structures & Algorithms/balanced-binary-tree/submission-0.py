# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # get height of left and right subtree
        # if height difference > 1, return false
        self.max_height = 0

        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)

            curr_height = abs(left_height - right_height)
            self.max_height = max(self.max_height, curr_height)
            return 1 + max(left_height, right_height)
        height(root)
        return False if self.max_height > 1 else True