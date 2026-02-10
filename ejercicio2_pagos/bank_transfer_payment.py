from payment_method import PaymentMethod


class BankTransferPayment(PaymentMethod):
    """
    Implementación concreta de pago por transferencia bancaria.
    """

    def pay(self, amount: float) -> None:
        print(f"Pago de ${amount} realizado por transferencia bancaria")
