import abc
from typing import Tuple


class WordListHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def import_word(self) -> Tuple[str, ...]:
        raise NotImplementedError()


class TupleWordListHandler(WordListHandler):
    def import_word(self) -> Tuple[str, ...]:
        return 'apple', 'banana'
