import abc


class BaseEntity(abc.ABC):

    def __init__(self, **kwargs):
        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

    def __repr__(self):
        return f'<{self.__class__.__name__}>'
