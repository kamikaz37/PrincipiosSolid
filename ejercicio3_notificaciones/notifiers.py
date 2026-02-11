# notifiers.py
from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod


# =========================
# Modelo de mensaje
# =========================
@dataclass(frozen=True)
class Notification:
    to: str
    title: str
    body: str


# =========================
# Interfaz (ISP)
# =========================
class Notifier(ABC):
    @abstractmethod
    def send(self, notification: Notification) -> None:
        """Envía una notificación por un canal."""
        ...


# =========================
# Implementaciones (SRP)
# =========================
class EmailNotifier(Notifier):
    def send(self, notification: Notification) -> None:
        print(f"[Email] To: {notification.to} | {notification.title} -> {notification.body}")


class SMSNotifier(Notifier):
    def send(self, notification: Notification) -> None:
        # Simulación de fallo si el número es inválido
        if not notification.to.startswith("+"):
            raise RuntimeError("Número inválido para SMS (debe empezar con +).")
        print(f"[SMS] To: {notification.to} | {notification.title} -> {notification.body}")


class PushNotifier(Notifier):
    def send(self, notification: Notification) -> None:
        print(f"[Push] To: {notification.to} | {notification.title} -> {notification.body}")


class SlackNotifier(Notifier):
    def send(self, notification: Notification) -> None:
        print(f"[Slack] Channel/User: {notification.to} | {notification.title} -> {notification.body}")
