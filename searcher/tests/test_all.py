from searcher.tests.test_data_sources import test_data_sources
from searcher.tests.test_matchers import test_matchers
from searcher.tests.test_rank_finders import test_rank_finders
from searcher.tests.test_searchers import test_searchers


def test_all():
    test_data_sources()
    test_matchers()
    test_rank_finders()
    test_searchers()
    print('All tests successfully completed')


if __name__ == '__main__':
    test_all()

