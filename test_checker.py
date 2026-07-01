import pytest

import checker
from checker import SimilarityChecker


@pytest.mark.parametrize("word1, word2, len_score", [
    ("ASD", "DSA", 60),
    ("A", "BB", 0),
    ("AAABB", "BAA", 20),
    ("AA", "AAE", 30)
])
def test_length(word1, word2, len_score):

    c = SimilarityChecker(word1, word2)
    assert c.get_length_similarity() == len_score
