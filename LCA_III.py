"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def ansMap(self, node):
        res = []
        
        while node:
            res.append(node.val)
            node = node.parent
        
        return res
    
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pMap = self.ansMap(p)
        
        while q:
            if q.val in pMap:
                return q
            else:
                q = q.parent