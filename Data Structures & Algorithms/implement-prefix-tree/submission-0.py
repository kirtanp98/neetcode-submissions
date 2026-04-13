class Trie:
    def __init__(self, value=None,terminating = False, children=None):
        self.value = value
        self.terminating = terminating
        self.children = children if children is not None else {}


class PrefixTree:

    def __init__(self):
        self.root = Trie()
        

    def insert(self, word: str) -> None:
        current = self.root
        
        firstLetter = word[0]
        if firstLetter not in current.children:
            current.children[firstLetter] = Trie()
            current = current.children[firstLetter]
        else:
            current = current.children[firstLetter]
        
        for i in range(1, len(word)):
            letter = word[i]
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

        if current.terminating:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        result = True
        current = self.root
        for i in prefix:
            if i not in current.children: 
                return False
            else:
                current = current.children[i]
        return result
        
        