class WordDictionary:

    def __init__(self):
        self.trie=[]
        

    def addWord(self, word: str) -> None:
        self.trie.append(word)

    def search(self, word: str) -> bool:
        for c in self.trie:
            if len(c) != len(word):
                continue
            i=0
            while i< len(c):
                if c[i] == word[i] or word[i]=='.':
                    i+=1
                else:
                    break
            if i== len(c):
                return True
        return False 
        
