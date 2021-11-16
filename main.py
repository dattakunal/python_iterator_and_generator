class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index=0
        self.words = sentence.split(' ')

    def __iter__(self):
        return self

    def __next__(self):

        if self.index==len(self.words):
            raise StopIteration

        current = self.words[self.index]
        self.index+=1
        
        return current

def GenWord(sentence):
    words = sentence.split(' ')

    for word in words:
        yield word


sentence = Sentence('This is a sentence')
#sentence = GenWord('This is a sentence')

for word in sentence:
    print(word)