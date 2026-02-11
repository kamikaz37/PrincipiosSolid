from payment_method import PaymentMethod
from typing import Dict, Any


class BankTransferPayment(PaymentMethod):
    """
    Implementación concreta de pago por transferencia bancaria.
    Aplica Liskov Substitution: es intercambiable con otros PaymentMethod.
    """

    def __init__(self, account_number: str = "****-****-1234", bank_name: str = "Banco Nacional"):
        self.account_number = account_number
        self.bank_name = bank_name

    def validate(self) -> bool:
        """Valida que la cuenta bancaria sea válida."""
        return len(self.account_number) >= 4 and len(self.bank_name) > 0

    def pay(self, amount: float) -> bool:
        """Procesa el pago por transferencia bancaria."""
        if not self.validate():
            print(f"❌ Error: Datos bancarios inválidos")
            return False
        
        if amount <= 0:
            print(f"❌ Error: El monto debe ser mayor a $0")
            return False
        
        if amount > 10000:
            print(f"❌ Error: Límite de transferencia excedido (máximo: $10000)")
            return False
        
        print(f"🏦 Procesando transferencia bancaria de ${amount:.2f}")
        print(f"   Banco: {self.bank_name}")
        print(f"   Cuenta: {self.account_number}")
        print(f"   Tiempo estimado: 1-3 días hábiles")
        print(f"✅ Transferencia iniciada correctamente")
        return True

    def get_payment_info(self) -> Dict[str, Any]:
        return {
            "metodo": "Transferencia Bancaria",
            "banco": self.bank_name,
            "cuenta": self.account_number
        }
