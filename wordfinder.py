import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    """read file line by line, return word, add word to list
    of already-read words, if nex towrk is in that list, read another one
    acces words /Users/student/words.txt
    prints out “[num-of-words-read] words read”

    >>> wf = WordFinder("/usr/share/dict/words")
    235976 words read

    """


    def __init__(self, file_of_words):
        self.file_of_words = file_of_words
        self.word_file = open(file_of_words)
        self.converted_list = self.convert_word_file_to_list(self.word_file)
        print(f"{len(self.converted_list)} words read")

    def convert_word_file_to_list(self, word_file):
        """convert self.word_file to list"""
        list_of_words = []
        for word in word_file:
            list_of_words.append(word.strip())
        return list_of_words

    def find_random_words(self):
        """find and return random word form converted list"""
        return random.choice(self.converted_list)
