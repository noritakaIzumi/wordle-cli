from wordle.word_list_handler import WordListHandler


class Wordle:
    def __init__(self, word_list_handler: WordListHandler):
        self.word_list_handler = word_list_handler
