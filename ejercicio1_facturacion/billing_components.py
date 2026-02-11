#modelos + interfaces + implementaciones

# billing_components.py
from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import date
from typing import Protocol


# Modelo de factura

@dataclass(frozen=True)
class Invoice:
    invoice_id: str
    customer_email: str
    customer_name: str
    amount: float
    issued_date: date


@dataclass(frozen=True)
class GeneratedDocument:
    """Representa el 'PDF' generado (simulado)."""
    filename: str
    content_bytes: bytes


# Interfaces (abstracciones) - DIP

class InvoiceGenerator(ABC):
    @abstractmethod
    def generate(self, invoice: Invoice) -> GeneratedDocument:
        ...


class InvoiceSender(ABC):
    @abstractmethod
    def send(self, invoice: Invoice, document: GeneratedDocument) -> None:
        ...


class InvoiceRepository(ABC):
    @abstractmethod
    def save(self, invoice: Invoice, document: GeneratedDocument) -> None:
        ...


# Implementaciones (SRP)
class PdfInvoiceGenerator(InvoiceGenerator):
    """Genera un PDF (aquí lo simulamos como bytes)."""

    def generate(self, invoice: Invoice) -> GeneratedDocument:
        filename = f"invoice_{invoice.invoice_id}.pdf"
        fake_pdf = (
            f"FACTURA {invoice.invoice_id}\n"
            f"Cliente: {invoice.customer_name}\n"
            f"Fecha: {invoice.issued_date}\n"
            f"Total: {invoice.amount}\n"
        ).encode("utf-8")

        return GeneratedDocument(filename=filename, content_bytes=fake_pdf)


class EmailInvoiceSender(InvoiceSender):
    """Envía factura por email (simulado)."""

    def send(self, invoice: Invoice, document: GeneratedDocument) -> None:
        print(
            f"[Email] Enviando {document.filename} a {invoice.customer_email} "
            f"(Cliente: {invoice.customer_name})"
        )


class WhatsAppInvoiceSender(InvoiceSender):
    """Ejemplo de extensión: envío por WhatsApp (simulado)."""

    def send(self, invoice: Invoice, document: GeneratedDocument) -> None:
        print(
            f"[WhatsApp] Enviando link/archivo {document.filename} a {invoice.customer_name}"
        )


class ApiInvoiceSender(InvoiceSender):
    """Ejemplo de extensión: envío a un API externo (simulado)."""

    def send(self, invoice: Invoice, document: GeneratedDocument) -> None:
        print(f"[API] POST /invoices -> {invoice.invoice_id} con {document.filename}")


class DatabaseInvoiceRepository(InvoiceRepository):
    """Guarda en base de datos (simulado)."""

    def save(self, invoice: Invoice, document: GeneratedDocument) -> None:
        print(f"[DB] Guardando invoice={invoice.invoice_id} y doc={document.filename}")


class FileInvoiceRepository(InvoiceRepository):
    """Guarda en archivos (simulado)."""

    def save(self, invoice: Invoice, document: GeneratedDocument) -> None:
        print(f"[File] Guardando {document.filename} en disco (simulado)")
