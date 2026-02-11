from payment_method import PaymentMethod
from typing import Dict, Any


class CryptoPayment(PaymentMethod):

    def __init__(self, wallet_address: str = "0x1A2B3C4D5E6F...", crypto_type: str = "Bitcoin"):
        self.wallet_address = wallet_address
        self.crypto_type = crypto_type
        self.confirmed = False

    def validate(self) -> bool:
        """Valida que la dirección de billetera sea válida."""
        return len(self.wallet_address) >= 10 and len(self.crypto_type) > 0

    def _confirm_blockchain(self) -> bool:
        """Simula la confirmación en la blockchain."""
        print(f"   ⛓️  Confirmando transacción en blockchain...")
        self.confirmed = True
        return True

    def pay(self, amount: float) -> bool:
        """Procesa el pago con criptomonedas."""
        if not self.validate():
            print(f"❌ Error: Dirección de billetera inválida")
            return False
        
        if amount <= 0:
            print(f"❌ Error: El monto debe ser mayor a $0")
            return False
        
        if amount > 50000:
            print(f"❌ Error: Límite de criptopago excedido (máximo: $50000)")
            return False
        
        print(f"₿ Procesando pago de ${amount:.2f} con {self.crypto_type}")
        print(f"   Billetera: {self.wallet_address}")
        
        if not self._confirm_blockchain():
            print(f"❌ Error: No se pudo confirmar la transacción en blockchain")
            return False
        
        print(f"   Confirmaciones: 3/3")
        print(f"✅ Pago exitoso con {self.crypto_type}")
        return True

    def get_payment_info(self) -> Dict[str, Any]:
        return {
            "metodo": f"Criptomoneda ({self.crypto_type})",
            "billetera": self.wallet_address,
            "estado": "Confirmado" if self.confirmed else "Pendiente"
        }
