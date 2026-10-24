from abc import ABC, abstractmethod


class Authorizer(ABC):
    @abstractmethod
    def authorize(self, amount: float) -> str:
        pass
