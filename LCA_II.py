class Solution:
    def check(self, root, node):
        if not root:
            return False
        
        left_ = right_ = False
        
        if root.val != node.val:
            
            if root.left:
                left_ = self.check(root.left, node)
            
            if root.right:
                right_ = self.check(root.right, node)
            
            return left_ or right_
        
        else:
            return True
        
    
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
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if self.check(root, p) and self.check(root, q):
            return self.LCA(root, p, q)
        
        else:
            return None