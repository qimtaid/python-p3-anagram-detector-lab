# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        matches = []
        for word in words:
            if sorted(self.word) == sorted(word):
                matches.append(word)
        return matches