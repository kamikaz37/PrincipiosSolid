from payment_method import PaymentMethod


class PaymentProcessor:
    """
    Procesador de pagos.
    Depende de la abstracción PaymentMethod, NO de clases concretas (DIP).
    Esto permite agregar nuevos métodos de pago sin modificar esta clase (OCP).
    """

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method
        self.transaction_history = []

    def process_payment(self, amount: float, description: str = "Compra") -> bool:
        """Procesa un pago usando el método de pago inyectado."""
        print(f"\n{'='*50}")
        print(f"Procesando: {description}")
        print(f"Monto: ${amount:.2f}")
        print(f"Método: {self.payment_method.get_payment_info()['metodo']}")
        print(f"{'='*50}")
        
        success = self.payment_method.pay(amount)
        
        if success:
            self.transaction_history.append({
                "amount": amount,
                "description": description,
                "method": self.payment_method.get_payment_info()["metodo"],
                "status": "Exitoso"
            })
        else:
            self.transaction_history.append({
                "amount": amount,
                "description": description,
                "method": self.payment_method.get_payment_info()["metodo"],
                "status": "Fallido"
            })
        
        return success

    def change_payment_method(self, new_method: PaymentMethod) -> None:
        """Permite cambiar el método de pago en tiempo de ejecución."""
        print(f"\n✏️ Cambiando método de pago a: {new_method.get_payment_info()['metodo']}")
        self.payment_method = new_method
