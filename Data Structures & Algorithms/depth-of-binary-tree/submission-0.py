# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(0, root)
    def helper(self, depth, root) -> int:
        if not root:
            return depth
        return max(self.helper(depth+1, root.left), self.helper(depth+1, root.right))