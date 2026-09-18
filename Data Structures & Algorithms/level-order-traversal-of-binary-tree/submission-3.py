from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()

                if node:
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

            if level:
                res.append(level)

        return res