import random

class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("/usr/share/dict/words")
    235976 words read

    """


    def __init__(self, file_of_words):
        """Open the file and read it ; print the number of words read and
        convert the file to a list of words"""
        self.word_file = open(file_of_words)

        self.list_of_words = self.convert_word_file_to_list(self.word_file)

        print(f"{len(self.list_of_words)} words read")

    def convert_word_file_to_list(self, word_file):
        """Convert the self.word_file to list of words with whitespace and line
        breaks removed"""
        return [word.strip() for word in word_file]

    def find_random_words(self):
        """Find and return a random word from the list_of_words"""
        return random.choice(self.list_of_words)

class SpecialWordFinder(WordFinder):
    """Accept a file of words and return a word that is not a space or
    in a #comment"""

    def __init__(self, file_of_words):
        """Inherit the initialized variables from the parent class"""
        super().__init__(file_of_words)

    def special_word():
        
        "insert method to strip symbols"super().find_random_words()




