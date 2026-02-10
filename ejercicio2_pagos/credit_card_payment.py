from payment_method import PaymentMethod


class CreditCardPayment(PaymentMethod):
    """
    Implementación concreta de pago con tarjeta de crédito.
    """

    def pay(self, amount: float) -> None:
        print(f"Pago de ${amount} realizado con tarjeta de crédito")
