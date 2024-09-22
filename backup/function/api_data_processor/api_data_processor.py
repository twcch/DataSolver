from abc import ABC, abstractmethod


class ApiDataProcessor(ABC):
    @abstractmethod
    def process_data(self):
        pass