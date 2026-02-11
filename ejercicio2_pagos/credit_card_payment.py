from payment_method import PaymentMethod
from typing import Dict, Any


class CreditCardPayment(PaymentMethod):
    """
    Implementación concreta de pago con tarjeta de crédito.
    Aplica Liskov Substitution: es intercambiable con otros PaymentMethod.
    """

    def __init__(self, card_number: str = "****-****-****-1234", cardholder: str = "Usuario"):
        self.card_number = card_number
        self.cardholder = cardholder

    def validate(self) -> bool:
        """Valida que la tarjeta tenga formato correcto."""
        return len(self.card_number) >= 4

    def pay(self, amount: float) -> bool:
        """Procesa el pago con tarjeta de crédito."""
        if not self.validate():
            print(f"❌ Error: Tarjeta de crédito inválida")
            return False
        
        if amount <= 0:
            print(f"❌ Error: El monto debe ser mayor a $0")
            return False
        
        print(f"💳 Procesando pago de ${amount:.2f} con tarjeta {self.card_number}")
        print(f"   Titular: {self.cardholder}")
        print(f"✅ Pago exitoso con tarjeta de crédito")
        return True

    def get_payment_info(self) -> Dict[str, Any]:
        return {
            "metodo": "Tarjeta de Crédito",
            "tarjeta": self.card_number,
            "titular": self.cardholder
        }
