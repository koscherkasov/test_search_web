from searcher.constants import LINEAR_TYPE_SEARCHER, INVERTED_INDEX_TYPE_SEARCHER
from searcher.searchers.base_searcher import Searcher
from searcher.utils import Book

EMPTY_QUERY = 'empty'
NOT_EMPTY_QUERY = 'cooking with cowgirl'
BOOKS_RESULT = (Book(id='B000SEIJE2',
                     title='Cooking with Convection: Everything You Need to Know to Get the Most from Your Convection '
                           'Oven',
                     rank=2,
                     words=[{'word': 'cooking', 'is_matching': True},
                            {'word': 'with', 'is_matching': True},
                            {'word': 'cowgirl', 'is_matching': False}]),
                Book(id='B000S1L8ZW',
                     title='Cowgirl Cuisine: Rustic Recipes and Cowgirl Adventures from a Texas Ranch',
                     rank=1,
                     words=[{'word': 'cooking', 'is_matching': False},
                            {'word': 'with', 'is_matching': False},
                            {'word': 'cowgirl', 'is_matching': True}]
                     ))


def test_searcher(type):
    # empty results
    Searcher.type = type
    result = Searcher.search(EMPTY_QUERY)
    books = result['results']
    assert len(books) == 0

    # not empty results
    result = Searcher.search(NOT_EMPTY_QUERY)
    books = result['results']
    assert len(books) == 2
    for i, book in enumerate(books):
        assert BOOKS_RESULT[i] == book


def test_searchers():
    test_searcher(type=LINEAR_TYPE_SEARCHER)
    test_searcher(type=INVERTED_INDEX_TYPE_SEARCHER)
    print('test_searchers successfully completed')


if __name__ == '__main__':
    test_searchers()
