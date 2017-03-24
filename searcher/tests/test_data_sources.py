from searcher.data_sources.file_data_source import CSVFileDataSource
from searcher.utils import Book

IDS = ('B000S1L8ZW', 'B000SEIJE2')
TITLES = ('Cowgirl Cuisine: Rustic Recipes and Cowgirl Adventures from a Texas Ranch',
          'Cooking with Convection: Everything You Need to Know to Get the Most from Your Convection Oven')


def test_csf_file_data_source():
    data_source = CSVFileDataSource(Book, 'test.tsv')

    for i, book in enumerate(data_source.get_object_generator()):
        assert isinstance(book, Book)
        assert book.id == IDS[i]
        assert book.title == TITLES[i]


def test_data_sources():
    test_csf_file_data_source()
    print('test_data_sources successfully completed')


if __name__ == '__main__':
    test_data_sources()
