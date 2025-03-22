def reverse_alternate_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if i % 2 != 0:
            words[i] = words[i][::-1]  
    return ' '.join(words)
input_sentence = "Hello world this is Python"
output_sentence = reverse_alternate_words(input_sentence)
print(output_sentence)  
