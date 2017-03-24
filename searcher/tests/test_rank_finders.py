from searcher.rank_finders.count_rank_finder import CountRankFinder

WORD_TO_INDEXES = {'a': (2, 3, 5), 'b': (6,)}


def test_count_rank_finder():
    rank = CountRankFinder.find(WORD_TO_INDEXES)
    assert rank == len(WORD_TO_INDEXES)


def test_rank_finders():
    test_count_rank_finder()
    print('test_rank_finders successfully completed')


if __name__ == '__main__':
    test_rank_finders()
