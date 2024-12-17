class TextProcessor:
    def __init__(self,text):
        self.text = text
    def split_into_sentence(self):
        sentences = []
        sentence = ""
        for char in self.text:
            sentence += char
            if char in ".!?":
                sentences.append(sentence.strip())
                sentence = ""
        return sentences
    def process_sentence(self):
        sentences = self.split_into_sentence()
        print("Processed Sentence Data:")
        for sentence in sentences:
            word_count = len(sentence.split())
            print(f"Sentence:{sentence},Word Count:{word_count}")
para = input("Enter your paragraph:")
txt = TextProcessor(para)
print("Split Sentences:")
sentences = txt.split_into_sentence()
for sentence in sentences:
    print(f"{sentence}")
txt.process_sentence()
