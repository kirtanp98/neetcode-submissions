# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
    def isSameTree(self, root, subroot):
        if root is None and subroot is None:
            return True

        if root and subroot and root.val == subroot.val:
            return self.isSameTree(root.right, subroot.right) and self.isSameTree(root.left, subroot.left)

        return False