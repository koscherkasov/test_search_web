import sys

from searcher.searchers.base_searcher import Searcher

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Run: python script.py <query>\n'
              '\twhere <query> is a search query\n'
              '\ti.q. python script.py Meal for')
        sys.exit(0)
    query = ' '.join(sys.argv[1:])
    result = Searcher.search(query)
    books = result['results']
    for book in books:
        print('{}\t{}\t{}\t{}'.format(book.id, book.title, book.rank, book.words))
