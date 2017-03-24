from itertools import chain

from collections import defaultdict


class InvertedIndexSearcher(object):
    def __init__(self, normalize, split, data_source, matcher, rank_finder):
        self.normalize = normalize
        self.split = split
        self.data_source = data_source
        self.object_cls = data_source.object_cls
        self.word_to_objects = defaultdict(set)
        self.init_word_to_objects()

    def init_word_to_objects(self):
        for row in self.data_source.get_object_generator():
            title = self.normalize(row.title)
            title_words = self.split(title)
            for title_word in title_words:
                self.word_to_objects[title_word].add(self.object_cls(id=row.id, title=row.title, rank=0))

    def search(self, query):
        """
        Search data by query from data source using 'inverted index' method

        @param query: search query
        @type query: str
        @return: dict with results = found a list of objects
        """
        query = self.normalize(query)
        query_words = self.split(query)

        obj_list_with_repetitions = list(chain(*[self.word_to_objects.get(query_word) for query_word in query_words]))

        result_object_ids = set()
        results = []
        for obj in obj_list_with_repetitions:
            if obj.id not in result_object_ids:
                query_words_full = [
                    {'word': word.lower(), 'is_matching': word in self.split(self.normalize(obj.title))} for word in
                    query_words]
                obj_with_rank = self.object_cls(id=obj.id,
                                                title=obj.title,
                                                rank=obj_list_with_repetitions.count(obj),
                                                words=query_words_full)
                result_object_ids.add(obj_with_rank.id)
                results.append(obj_with_rank)

        results.sort(key=lambda b: b.rank, reverse=True)

        return dict(results=results)
