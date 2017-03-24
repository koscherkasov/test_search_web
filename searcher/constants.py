from searcher.searchers.inverted_index_searcher import InvertedIndexSearcher
from searcher.searchers.linear_searcher import LinearSearcher

LINEAR_TYPE_SEARCHER = 'linear'
INVERTED_INDEX_TYPE_SEARCHER = 'inverted_index'

TYPE_TO_SEARCHER = {LINEAR_TYPE_SEARCHER: LinearSearcher,
                    INVERTED_INDEX_TYPE_SEARCHER: InvertedIndexSearcher}
