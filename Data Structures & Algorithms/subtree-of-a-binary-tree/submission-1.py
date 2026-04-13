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
        # no tree is always a subtree

        if self.isSubtreeSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSubtreeSame(self, root, subRoot) -> bool:
        if root is None and subRoot is None:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.isSubtreeSame(root.right, subRoot.right) and self.isSubtreeSame(root.left, subRoot.left)
        
        return False