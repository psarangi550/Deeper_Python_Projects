class SentenceGen(object):
    def __init__(self,sentence_val):
        self.sentence_val = sentence_val
    def __iter__(self):
        list_val=self.sentence_val.split()
        for item in list_val:
            yield item

sent_gen=SentenceGen("My Name is  Pratik")

for item in sent_gen:
    print(item)