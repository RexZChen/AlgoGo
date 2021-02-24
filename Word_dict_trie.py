class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}  # str
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("*")
        

    def addWord(self, word: str) -> None:
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode(letter)
            current_node = current_node.children[letter]
        
        current_node.end_of_word = True
        
    def dfs(self, index, node, word):
        if index == len(word):
            return node.end_of_word
        
        if word[index] == ".":
            for kid in node.children:
                if self.dfs(index+1, node.children[kid], word):
                    return True
            return False
        
        elif word[index] not in node.children:
            return False
        
        else:
            return self.dfs(index+1, node.children[word[index]], word)
        
            
    
    
    def search(self, word: str) -> bool:
        return self.dfs(index=0, node=self.root, word=word)
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)