from abc import ABCMeta, abstractmethod

class IObservable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """the subscribe method"""

    @staticmethod
    @abstractmethod
    def unsubcribe(observer):
        """the unsubribe method"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """the notify method"""

class Subject(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubcribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *argh, **kwargs):
        for observer in self._observers:
            observer.notify(self, *argh, **kwargs)

class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(observable, *args, **kwargs):
        """recevie notification"""

#concrete observer
class Observer(IObserver):
    def __init__(self, observable):
       observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print("observer received", args, kwargs)

#client
SUBJECT = Subject()

OBSERVERa = Observer(SUBJECT)
OBSERVERb = Observer(SUBJECT)

SUBJECT.notify("hello subscriber")