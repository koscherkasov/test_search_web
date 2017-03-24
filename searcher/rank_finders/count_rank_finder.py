class CountRankFinder(object):
    @staticmethod
    def find(query_word_to_indexes):
        """
        Return rank based on count found words

        @param query_word_to_indexes: dict with key - found words, value - iterable of indexes this word found
        @type query_word_to_indexes: dict
        @return: int rank
        """
        return len(query_word_to_indexes)
