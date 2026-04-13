class Trie:
    def __init__(self, terminating = False, children=None):
        self.terminating = terminating
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        current = self.root

        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                current.children[letter] = Trie()
                current = current.children[letter]
        
        current.terminating = True
        

    def search(self, word: str) -> bool:
        current = self.root
        return self.helper(current, word)
        
    def helper(self, node: Trie, word:str) -> bool:
        current = node

        for i, letter in enumerate(word):
            if letter in current.children:
                current = current.children[letter]
            elif letter == ".":
                for child in current.children.values():
                    if self.helper(child, word[i+1:]):
                        return True
                return False
            else:
                return False
        
        return current.terminating
