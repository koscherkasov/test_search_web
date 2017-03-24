import os
from collections import namedtuple

Book = namedtuple('Book', ['id', 'title', 'rank', 'words'])


def upper_case(text):
    """
    Get upper case modified text

    @param text: text that will be modified
    @type text: str
    @return: upper case modified text
    """
    return text.upper()


def space_split(text):
    """
    Get words from text divided by space

    @param text: text that will be divided
    @type text: str
    @return: tuple of divided text
    """
    return tuple(text.split())


def get_occurrences(value, iterable):
    """
    Get indexes all occurrences value in iterable

    @param value:
    @param iterable: iterable object where value will be find
    @type iterable: iterable
    @return: tuple of indexes all occurrences value in iterable
    """
    return tuple((i for i, source in enumerate(iterable) if value == source))


def get_full_file_names(directory=None, extension=None):
    """
    Get full name of files in directory with extensions.
    If argument directory was not given search will be implemented in the current directory
    If argument extension was not given will be returned all file names in the directory

    @param directory: directory
    @type directory: str
    @param extension: extensions of file i.g. '.txt'
    @type extension: str
    @return: tuple of full file names
    """
    if not directory:
        directory = os.getcwd()
    file_names = filter(lambda x: x.endswith(extension), os.listdir(directory)) if extension else os.listdir(directory)
    return tuple((os.path.join(directory, file_name) for file_name in file_names))



