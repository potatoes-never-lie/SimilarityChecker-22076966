import math

class SimilarityChecker:

    LENGTH_MULTIPLIER = 60

    def __init__(self, word1:str, word2:str):
        self.word1 : str = word1
        self.word2 : str = word2

    def get_length_similarity(self) -> float:
        _word1_length = len(self.word1)
        _word2_length = len(self.word2)

        _gap = abs(_word1_length - _word2_length)
        _short_length = min(_word1_length, _word2_length)

        return round((1 - (_gap / _short_length)) * self.LENGTH_MULTIPLIER, 3)
