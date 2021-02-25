class TrieNode:
    def __init__(self):
        self.children = dict()
        self.val = 0

class Trie:
    def __init__(self, n):
        self.root = TrieNode()
        self.n = n
    
    def add_num(self, num):
        self._add(num)
    
    def _add(self, num):
        node = self.root
        
        for bit in range(self.n, -1, -1):
            if num & (1 << bit):
                val = 1
            else:
                val = 0
            
            if val not in node.children:
                node.children[val] = TrieNode()
            
            node = node.children[val]
        
        node.val = num
        
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_len = len(bin(max(nums))) - 2
        trie_tree = Trie(max_len)
        
        for num in nums:
            trie_tree.add_num(num)
            
        res = 0
        
        for num in nums:
            node = trie_tree.root
            
            for bit in range(max_len, -1, -1):
                if num & (1 << bit):
                    val = 1
                else:
                    val = 0
                
                if (1 - val) in node.children:
                    node = node.children[1 - val]
                else:
                    node = node.children[val]
                
            res = max(res, num ^ node.val)
            
        
        return res
        