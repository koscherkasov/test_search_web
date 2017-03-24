from searcher.matchers.simple_matcher import SimpleMatcher

QUERY_WORDS = ('a', 'b')
SOURCE_WORDS = ('q', 'w', 'a', 'a', 'w', 'a', 'b')
WORD_TO_INDEXES = {'a': (2, 3, 5), 'b': (6,)}


def test_simple_matcher():
    word_to_indexes = SimpleMatcher.get_word_to_indexes(QUERY_WORDS, SOURCE_WORDS)
    assert word_to_indexes == WORD_TO_INDEXES


def test_matchers():
    test_simple_matcher()
    print('test_matchers successfully completed')


if __name__ == '__main__':
    test_matchers()
