import csv

from searcher.data_sources.data_source import DataSource
from searcher.utils import get_full_file_names

DELIMITER_TO_EXTENSION = {'\t': '.tsv', ',': '.csv'}


class CSVFileDataSource(DataSource):
    """Data source class for reading from CSV files"""
    def __init__(self, object_cls, file_name=None, delimiter='\t'):
        """
        Initialization instance of CSVFileDataSource

        @param object_cls: class which instances will be returned
        @param file_name: file name
        @type file_name: str
        @param delimiter: delimiter for csv file
        @type delimiter: str
        """
        super().__init__(object_cls)
        self.delimiter = delimiter
        self.file_name = file_name if file_name else \
            get_full_file_names(extension=DELIMITER_TO_EXTENSION.get(delimiter))[0]

    def get_object_generator(self):
        """
        Generator yielded object_cls instances from csv file

        @return: yield object_cls instance
        """
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            for line in csv_reader:
                yield self.object_cls(id=line[0], title=line[1], rank=None, words=None)
