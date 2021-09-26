from abc import ABCMeta, abstractmethod


def event(callback):
    pass


class BirdEyeView(metaclass=ABCMeta):
    @abstractmethod
    def getImage(self):
        pass