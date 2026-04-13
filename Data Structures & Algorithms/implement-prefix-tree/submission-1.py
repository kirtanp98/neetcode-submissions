class Trie:
    def __init__(self, terminating = False, children=None):
        self.terminating = terminating
        self.children = children if children is not None else {}


class PrefixTree:

    def __init__(self):
        self.root = Trie()
        
    def insert(self, word: str) -> None:
        current = self.root
        
        for letter in word:
            if letter not in current.children: 
                current.children[letter] = Trie()
                current = current.children[letter]
            else:
                current = current.children[letter]

        current.terminating = True
        return


    def search(self, word: str) -> bool:
        current = self.root
        for i in word:
            if i not in current.children: 
                return False
            else:
                current = current.children[i]

        return current.terminating
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in prefix:
            if i not in current.children: 
                return False
            else:
                current = current.children[i]
        return True
        
        