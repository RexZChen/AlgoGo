# Sol 1

class Node:
    def __init__(self, v):
        self.minValue = v
        self.left = None
        self.right = None

class Solution:
    def addValue(self, root, val2add):
        current_node = root
        
        for i in range(31):
            current_node.minValue = min(current_node.minValue, val2add)
            
            if val2add & (1 << (30-i)) > 0:
                
                if current_node.right == None:
                    current_node.right = Node(val2add)
                    
                current_node = current_node.right
                
            else:
                if current_node.left == None:
                    current_node.left = Node(val2add)
                    
                current_node = current_node.left

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        root = Node(0)
        
        for num in nums:
            self.addValue(root, num)  # build the tree
            
        res = []
        
        for q in queries:
            current_node = root
            
            for i in range(31):
                if current_node == None or current_node.minValue > q[1]:
                    current_node = None
                    break
                    
                if current_node.left is None and current_node.right is not None:
                    current_node = current_node.right
                    continue
                    
                if current_node.right is None and current_node.left is not None:
                    current_node = current_node.left
                    continue
                    
                    
                if q[0] & (1 << (30-i)) > 0:
                    current_node = current_node.left
                    
                elif current_node.right.minValue > q[1]:
                    current_node = current_node.left
                    
                else:
                    current_node = current_node.right
                    
            if current_node is None:
                res.append(-1)
                
            else:
                res.append(q[0] ^ current_node.minValue)
                
        return res

## Sol 2

class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, num):
        current_node = self.root
        
        for i in range(31, -1, -1):
            cur_val = (num >> i) & 1
            
            if cur_val not in current_node:
                current_node[cur_val] = {}
                
            current_node = current_node[cur_val]
                
    def query(self, num):
        if not self.root: 
            return -1
        
        current_node, res = self.root, 0
        
        for i in range(31, -1, -1):
            cur_val = (num >> i) & 1
            
            if 1 - cur_val in current_node:
                current_node = current_node[1 - cur_val]
                res = res | (1 << i)
                
            else:
                current_node = current_node[cur_val]
                
        return res

class Solution:
    
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        trie = Trie()
        
        ans = [-1] * len(queries)
        
        count = 0
        
        for i, (x, m) in queries:
            
            while count < len(nums) and nums[count] <= m:
                trie.insert(nums[count])
                count += 1
                
            ans[i] = trie.query(x)
            
        return ans
            
            
        
        
        