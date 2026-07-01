import math

class SimilarityChecker:

    LENGTH_MULTIPLIER = 60
    ALPHA_MULTIPLIER = 40

    def __init__(self, word1:str, word2:str):
        self.word1 : str = word1
        self.word2 : str = word2

    def get_length_similarity(self) -> float:
        _word1_length = len(self.word1)
        _word2_length = len(self.word2)

        _gap = abs(_word1_length - _word2_length)
        _short_length = min(_word1_length, _word2_length)

        return round((1 - (_gap / _short_length)) * self.LENGTH_MULTIPLIER, 3)

    @property
    def same_letters_cnt(self) -> int:
        same_letters = set(self.word1) & set(self.word2)
        return len(same_letters)

    @property
    def total_letters_cnt(self) -> int:
        total_letters = set(self.word1) | set(self.word2)
        return len(total_letters)

    def get_alpha_similarity(self):
        return round(self.same_letters_cnt / self.total_letters_cnt * self.ALPHA_MULTIPLIER, 3)
