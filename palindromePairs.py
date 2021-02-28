class Trie:
    def __init__(self):
        self.is_end = "*"
        self.index = "/"
        self.root = {} # dict
    
    
    def insert(self, word, index):
        # Insert word in the trie
        
        node = self.root
        
        for char in word:
            if char not in node:
				# If the char does not exist on the node
				# initialize it with a dict
                node[char] = {}
            node = node[char]
            
        node[self.is_end] = True
        node[self.index] = index
    
    
    def search(self, word):
        # Searches the word on the trie
        # if it exists returns True if it
        # is a leaf and the index of the word
        
        node = self.root
        
        for char in word:
            if char not in node:
                return False, -1
            node = node[char]
            
        return node.get(self.is_end, False), node.get(self.index, -1)
            

            
class Solution:
    def is_valid_palindrome(self, word):
        left, right = 0, len(word)-1
        
        while left<right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
            
        return True
        
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Init the trie
        trie = Trie()
        result = []

        # Insert the words in the trie
        for i, word in enumerate(words):
            trie.insert(word, i)

        # Iterate over the given words
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                # Split the word in two parts
                left_part, right_part = word[:j], word[j:]

                # If the first part of the left part is a palindrome
                # Search for the complement of the right part.
                # e.g. word -> ssabc and j = 2
                #  if ss is a paindrome search the complement of 
                # abc, which is cba.
                # This means the palindrome of the pair is cbassabc
                if self.is_valid_palindrome(left_part): 
                    flag, index = trie.search(right_part[::-1])
                    if flag and i!=index:
                        result.append([index, i])

                # Verify right part is not empty to avoid repeated results
                # and repeat the same process for the other part of the string
                if right_part and self.is_valid_palindrome(right_part):
                    flag, index = trie.search(left_part[::-1])
                    if flag and i!=index:
                        result.append([i, index])

        return result