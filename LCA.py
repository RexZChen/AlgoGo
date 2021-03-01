# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
                
            elif root.val < p.val and root.val < q.val:
                root = root.right
            
            else:
                return root
            
#     LCA in Binary Tree:
#     def LCA(root, p, q):
        
# 	    if p == root or q == root:
# 		    return root

# 	    left = right = None

# 	    if root.left:
# 		    left = LCA(root.left, p, q)
# 	    if root.right:
# 		    right = LCA(root.right, p, q)

# 	    if not left:
# 		    return right
# 	    if not right:
# 		    return left

# 	    return root