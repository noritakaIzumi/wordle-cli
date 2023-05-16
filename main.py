# ゲームスタート
import random

from wordle.input_handler import CliInputHandler
from wordle.word_list_handler import TupleWordListHandler

input_handler = CliInputHandler()
word_list_handler = TupleWordListHandler()
word_list = word_list_handler.import_word()

answer: str = random.choice(word_list)
limit = 6

while limit > 0:
    limit -= 1
    word = input_handler.get_input('Enter word')
    if word not in word_list:
        print('not a word')
        continue
    # TODO: 判定
    if word == answer:
        print('correct')
        break
    else:
        print('incorrect')
