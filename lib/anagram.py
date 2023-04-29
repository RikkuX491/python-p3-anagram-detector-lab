# your code goes here!

class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, list):
        return [word for word in list if(self.is_anagram(word))]
    
    def is_anagram(self, word):
        if(not len(word) == len(self.word)):
            return False
        
        for letter in word:
            if not letter in self.word:
                return False
        return True