from payment_method import PaymentMethod


class PayPalPayment(PaymentMethod):
    """
    Implementación concreta de pago con PayPal.
    """

    def pay(self, amount: float) -> None:
        print(f"Pago de ${amount} realizado con PayPal")
