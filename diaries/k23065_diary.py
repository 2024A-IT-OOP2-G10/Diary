from abc import ABC, abstractmethod

class k23065_Diary(ABC):

    @abstractmethod
    def get_date(self):
        return"2024-11-28"

    @abstractmethod
    def get_summary(self):
        return"釣りに行った。アジが100匹釣れた"

    @abstractmethod
    def get_author(self):
        return"杉山大晴"
