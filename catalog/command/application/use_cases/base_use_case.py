import abc


class BaseUseCase(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        pass
