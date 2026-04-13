# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBST(root, -2000, 2000)

    def isBST(self, root, low, high) -> bool:
        if root is None:
            return True

        if not (low < root.val < high):
            return False
        
        return self.isBST(root.left, low, root.val) and self.isBST(root.right, root.val, high)