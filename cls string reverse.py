print("\033c")

class Word:
    def __init__(self, word):  
        self.word = word

    def revStr(self):
        return self.word[::-1]  


w1 = input("Enter a word: ")


word_obj = Word(w1)

print("Reversed word:", word_obj.revStr())

