from payment_method import PaymentMethod


class PaymentProcessor:
    """
    Procesador de pagos.
    Depende de la abstracción PaymentMethod (DIP).
    """

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount: float) -> None:
        self.payment_method.pay(amount)
