from nlplogic.corenlp import get_phrases


def test_get_phrase():
    assert "golden state" in get_phrases("Goldne State Warriors")
