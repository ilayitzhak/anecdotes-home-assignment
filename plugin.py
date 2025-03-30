from abc import abstractmethod


class Plugin:
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def run(self):
        raise NotImplementedError("Subclasses should implement this method.")