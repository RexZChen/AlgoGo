class TrieNode():
    def __init__(self):
        self.children = {}
        self.weights = []

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, i):
        node = self.root
        node.weights.append(i)
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                
            node = node.children[char]
            node.weights.append(i)
    
    def search(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                return []
            
            node = node.children[char]
            
        return node.weights
        
class WordFilter:
    def __init__(self, words: List[str]):
        self.prefix, self.suffix = Trie(), Trie()
        
        i, n = 0, len(words)
        
        while i < n:
            w = words[i]
            self.prefix.insert(w, i)
            self.suffix.insert(w[::-1], i)
            i += 1

    def f(self, prefix: str, suffix: str) -> int:
        pre = self.prefix.search(prefix)
        suf = self.suffix.search(suffix[::-1])
        i, j = len(pre) - 1, len(suf) - 1
        
        while i >= 0 and j >= 0:
            if pre[i] == suf[j]:
                return pre[i]
            
            elif pre[i] < suf[j]:
                j -= 1
                
            else:
                i -= 1
                
        return -1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)