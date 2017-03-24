class DataSource(object):
    """Base class for data source"""

    def __init__(self, object_cls):
        """
        @param object_cls: class which instances will be returned
        """
        self.object_cls = object_cls

    def get_object_generator(self):
        raise NotImplementedError()
