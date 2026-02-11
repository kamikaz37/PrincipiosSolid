from payment_method import PaymentMethod
from typing import Dict, Any


class PayPalPayment(PaymentMethod):
    """
    Implementación concreta de pago con PayPal.
    Aplica Liskov Substitution: es intercambiable con otros PaymentMethod.
    """

    def __init__(self, email: str = "usuario@example.com"):
        self.email = email
        self.connected = False

    def validate(self) -> bool:
        """Valida que el email de PayPal sea válido."""
        return "@" in self.email and "." in self.email


    def pay(self, amount: float) -> bool:
        """Procesa el pago con PayPal."""
        if not self.validate():
            print(f"❌ Error: Email de PayPal inválido: {self.email}")
            return False
        
        if amount <= 0:
            print(f"❌ Error: El monto debe ser mayor a $0")
            return False
        
        if not self._connect_to_paypal():
            print(f"❌ Error: No se pudo conectar con PayPal")
            return False
        
        print(f"🌐 Procesando pago de ${amount:.2f} con PayPal")
        print(f"   Cuenta: {self.email}")
        print(f"✅ Pago exitoso con PayPal")
        return True

    def get_payment_info(self) -> Dict[str, Any]:
        return {
            "metodo": "PayPal",
            "email": self.email,
            "estado": "Conectado" if self.connected else "Desconectado"
        }
