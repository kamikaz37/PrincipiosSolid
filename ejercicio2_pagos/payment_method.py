from abc import ABC, abstractmethod
from typing import Dict, Any


class PaymentMethod(ABC):
    """
    Abstracción para los métodos de pago.
    Define el contrato que deben cumplir todos los métodos de pago.
    Aplica Dependency Inversion y Open/Closed.
    """

    @abstractmethod
    def validate(self) -> bool:
        """Valida que el método de pago esté correctamente configurado."""
        pass

    @abstractmethod
    def pay(self, amount: float) -> bool:
        """Procesa el pago. Retorna True si fue exitoso, False en caso contrario."""
        pass

    @abstractmethod
    def get_payment_info(self) -> Dict[str, Any]:
        """Retorna información sobre el método de pago."""
        pass
