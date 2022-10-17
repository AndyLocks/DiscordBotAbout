import json
from set import Setter
from get import Getter

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Basa(Setter, Getter, metaclass=Singleton):
    def __init__(self,basa: str):
        self.url = basa