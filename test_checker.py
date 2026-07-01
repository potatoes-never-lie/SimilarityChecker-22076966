import pytest

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

@pytest.mark.parametrize("word1, word2, alpha_score", [
    ("ASD", "DSA", 40),
    ("A", "BB", 0),
    ("AAABB", "BAA", 40),
    ("AA", "AAE", 20)
])
def test_alpha(word1, word2, alpha_score):

    c = SimilarityChecker(word1, word2)
    assert c.get_alpha_similarity() == alpha_score

def test_invalid_words():
    with pytest.raises(ValueError):
        sc = SimilarityChecker("", "")
        sc.get_length_similarity()
