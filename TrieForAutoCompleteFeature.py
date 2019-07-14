# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []
        
    def formTrie(self, keys):
        for key in keys:
            self.insert(key)
    
    def insert(self, key):
        node = self.root
        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
        node.last = True
        
    def search(self, key):
        node = self.root
        found = True
        for a in list(key):
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
        return node and node.last and found
        
    def suggestRec(self, node, word):
        if node.last:
            self.word_list.append(word)
        for a, nextnode in node.children.items():
            self.suggestRec(nextnode, word + a)
            
    def autoComplete(self, key):
        node = self.root
        not_found = False
        temp_word = ''
        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break
            temp_word += a
            node = node.children[a]
        if not_found:
            return 0
        elif node.last:
            return -1
        self.suggestRec(node, temp_word)
        for s in self.word_list:
            print(s)
        return 1
        
# Driver Code 
keys = ["ankur", "ankit", "anshul", "anubhav", "amit",  
        "aftab", "animesh", "ankita", "xyz"] # keys to form the trie structure. 
key = "ank" # key for autocomplete suggestions. 
  
# creating trie object 
t = Trie() 
  
# creating the trie structure with the  
# given set of strings. 
t.formTrie(keys) 
  
# autocompleting the given key using  
# our trie structure. 
comp = t.autoComplete(key) 
  
if comp == -1: 
    print("No other strings found with this prefix\n") 
elif comp == 0: 
    print("No string found with this prefix\n")