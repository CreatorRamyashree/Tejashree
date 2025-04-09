class StringReverser:
    def reverse_words(self, sentence):
        words = sentence.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

reverser = StringReverser()
user_input = input("Enter a sentence: ")
result = reverser.reverse_words(user_input)
print(result)
