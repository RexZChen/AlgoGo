# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def LCA(self, root, p, q):
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left_res, right_res = None, None
        
        left_res = self.LCA(root.left, p, q)
        right_res = self.LCA(root.right, p, q)
        
        if not left_res:
            return right_res
        
        if not right_res:
            return left_res
        
        return root
    
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if len(nodes) == 1:
            return nodes[0]
        
        if len(nodes) == 2:
            return self.LCA(root, nodes[0], nodes[1])
        
        # len > 2
        
        while len(nodes) > 2:
            # temp_left = nodes.pop()
            # temp_right = nodes.pop()
            
            nodes.append(self.LCA(root, nodes.pop(), nodes.pop()))
        
        # assert len(nodes) == 2
        return self.LCA(root, nodes[0], nodes[1])