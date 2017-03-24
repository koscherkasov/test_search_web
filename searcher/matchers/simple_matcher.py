from searcher.utils import get_occurrences


class SimpleMatcher(object):
    @staticmethod
    def get_word_to_indexes(query_words, source_words):
        """
        Find every query word from query_words list in source_words list
        And return dict with key - found words, value - list of indexes this word found

        @param query_words: iterable of query words
        @type query_words: iterable of str
        @param source_words: iterable of source words
        @type source_words: iterable of str
        @return: dict with key - found words, value - list of indexes this word found
        """
        word_to_indexes = dict()
        for query_word in query_words:
            occurrences = get_occurrences(query_word, source_words)
            if occurrences:
                word_to_indexes[query_word] = occurrences
        return word_to_indexes
