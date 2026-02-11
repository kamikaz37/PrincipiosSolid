from credit_card_payment import CreditCardPayment
from paypal_payment import PayPalPayment
from bank_transfer_payment import BankTransferPayment
from crypto_payment import CryptoPayment
from payment_processor import PaymentProcessor


def print_section(title: str):
    """Imprime un título de sección."""
    print(f"\n{'#'*60}")
    print(f"# {title.center(56)} #")
    print(f"{'#'*60}")


def main():
    print_section("PLATAFORMA DE PAGOS - DEMO PRINCIPIOS SOLID")
    
    # 1. Demostración: Tarjeta de Crédito
    print_section("1. PAGO CON TARJETA DE CRÉDITO")
    card = CreditCardPayment(
        card_number="****-****-****-4532",
        cardholder="Juan García"
    )
    processor = PaymentProcessor(card)
    processor.process_payment(230.00, "Compra de laptop")
    
    # 2. Demostración: PayPal
    print_section("2. PAGO CON PAYPAL")
    paypal = PayPalPayment(email="cliente@gmail.com")
    processor.change_payment_method(paypal)
    processor.process_payment(99.99, "Compra de software")
    
    # 3. Demostración: Transferencia Bancaria
    print_section("3. PAGO POR TRANSFERENCIA BANCARIA")
    bank = BankTransferPayment(
        account_number="****-****-5678",
        bank_name="Banco Latinoamericano"
    )
    processor.change_payment_method(bank)
    processor.process_payment(1500.00, "Pago a proveedor")
    
    # 4. Demostración: Criptomonedas (Nueva pasarela - sin modificar código existente)
    print_section("4. PAGO CON CRIPTOMONEDAS (Nueva pasarela)")
    crypto = CryptoPayment(
        wallet_address="0x1A2B3C4D5E6F7G8H...",
        crypto_type="Bitcoin"
    )
    processor.change_payment_method(crypto)
    processor.process_payment(500.00, "Compra de activos digitales")
    
    # 5. Validación de errores
    print_section("5. MANEJO DE ERRORES")
    
    invalid_card = CreditCardPayment(
        card_number="123",
        cardholder="Usuario"
    )
    processor.change_payment_method(invalid_card)
    processor.process_payment(100.00, "Intento con tarjeta inválida")
    
    # 6. Monto negativo
    valid_card = CreditCardPayment()
    processor.change_payment_method(valid_card)
    processor.process_payment(-50.00, "Intento con monto negativo")
    
    # 7. Límite de transferencia
    print_section("6. VALIDACIONES DE LÍMITES")
    bank_transfer = BankTransferPayment()
    processor.change_payment_method(bank_transfer)
    processor.process_payment(15000.00, "Intento que excede límite bancario")
    
    # 8. Historial de transacciones
    print_section("7. HISTORIAL DE TRANSACCIONES")
    print(f"\n{'Descripción':<35} {'Monto':<12} {'Estado':<12}")
    print(f"{'-'*59}")
    
    for tx in processor.transaction_history:
        status_emoji = "✅" if tx["status"] == "Exitoso" else "❌"
        print(f"{tx['description']:<35} ${tx['amount']:<11.2f} {status_emoji} {tx['status']:<8}")
    


if __name__ == "__main__":
    main()
