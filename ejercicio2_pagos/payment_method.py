from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """
    Abstracción para los métodos de pago.
    Aplica Dependency Inversion y Open/Closed.
    """

    @abstractmethod
    def pay(self, amount: float) -> None:
        pass
