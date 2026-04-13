# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
           # Build hashmap for inorder indices
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        self.pre_idx = 0
        
        def helper(left, right):
            if left > right:
                return None
            
            # Pick current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            # Find pivot using hashmap (O(1))
            pivot = inorder_map[root_val]
            
            # Build left and right subtree
            root.left = helper(left, pivot - 1)
            root.right = helper(pivot + 1, right)
            
            return root
        
        return helper(0, len(inorder) - 1)