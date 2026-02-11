# servicio central + inyección + demo

from datetime import date
from billing_components import (
    Invoice,
    InvoiceGenerator,
    InvoiceSender,
    InvoiceRepository,
    PdfInvoiceGenerator,
    EmailInvoiceSender,
    WhatsAppInvoiceSender,
    ApiInvoiceSender,
    DatabaseInvoiceRepository,
    FileInvoiceRepository,
)


# Servicio central (DIP + SRP)
# - Orquesta el proceso: generar -> guardar -> enviar
# - Depende de abstracciones, no de clases concretas

class BillingService:
    def __init__(
        self,
        generator: InvoiceGenerator,
        sender: InvoiceSender,
        repository: InvoiceRepository,
    ) -> None:
        self._generator = generator
        self._sender = sender
        self._repository = repository

    def process_invoice(self, invoice: Invoice) -> None:
        document = self._generator.generate(invoice)
        self._repository.save(invoice, document)
        self._sender.send(invoice, document)


# Demo

def demo() -> None:
    invoice = Invoice(
        invoice_id="A-1001",
        customer_email="cliente@email.com",
        customer_name="Cliente Demo",
        amount=250000.0,
        issued_date=date.today(),
    )

    # Caso 1: PDF + DB + Email
    service_email = BillingService(
        generator=PdfInvoiceGenerator(),
        sender=EmailInvoiceSender(),
        repository=DatabaseInvoiceRepository(),
    )
    service_email.process_invoice(invoice)

    print("\n--- Cambiar canal de envío sin tocar BillingService (OCP) ---")

    # Caso 2: PDF + DB + WhatsApp
    service_whatsapp = BillingService(
        generator=PdfInvoiceGenerator(),
        sender=WhatsAppInvoiceSender(),
        repository=DatabaseInvoiceRepository(),
    )
    service_whatsapp.process_invoice(invoice)

    print("\n--- Cambiar almacenamiento sin tocar BillingService ---")

    # Caso 3: PDF + File + API
    service_api_file = BillingService(
        generator=PdfInvoiceGenerator(),
        sender=ApiInvoiceSender(),
        repository=FileInvoiceRepository(),
    )
    service_api_file.process_invoice(invoice)


if __name__ == "__main__":
    demo()
