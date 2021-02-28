class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.end = False
        self.word = ""  # 存储当当前的语料
        self.times = 0
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, sentence, times):
        node = self.root
        
        for char in sentence:
            node = node.child[char]
            
        if not node.end:
            node.end = True
            node.word = sentence
            
            node.times = times if times else 1
            
        else:
            node.times += 1
        
    def search(self, word):  # 直接递归也可以
        res = [] 
        res_dic = {}  # 存储所有备选的res 用于sort
        
        node = self.root
        
        for char in word:
            if char not in node.child:
                return None
            node = node.child[char]
            
        stack = []
        stack.append(node)
        
        #### DFS ####
        while stack:
            node = stack.pop()
            if node.end:
                res_dic[node.word] = node.times
            for ch in node.child:
                n = node.child[ch]
                stack.append(n)
            
        max_len = 3
        for key, _ in sorted(res_dic.items(), key=lambda x:(-x[1],x[0])):
        
            if max_len == 0:
                break
                
            res.append(key)
            max_len -= 1
            
        return res
        
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.input_ = ""
        self.trie = Trie()
        
        for sentence,time in zip(sentences,times):
            self.trie.insert(sentence, time)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.input_, None)
            self.input_ = ""
            return []
        
        self.input_ += c
        
        return self.trie.search(self.input_)
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)