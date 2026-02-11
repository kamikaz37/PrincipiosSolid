# app.py
from notifiers import (
    Notification,
    Notifier,
    EmailNotifier,
    SMSNotifier,
    PushNotifier,
    SlackNotifier,
)


# =========================
# Servicio central (DIP)
# - Depende de la abstracción Notifier, no de clases concretas.
# =========================
class NotificationService:
    def __init__(self, notifier: Notifier) -> None:
        self._notifier = notifier

    def notify(self, to: str, title: str, body: str) -> None:
        notification = Notification(to=to, title=title, body=body)
        self._notifier.send(notification)


# =========================
# Variante útil: múltiples canales con tolerancia a fallos
# (opcional, pero demuestra qué pasa si un canal falla)
# =========================
class MultiChannelNotificationService:
    def __init__(self, notifiers: list[Notifier]) -> None:
        self._notifiers = notifiers

    def notify_all(self, to: str, title: str, body: str) -> None:
        notification = Notification(to=to, title=title, body=body)

        for notifier in self._notifiers:
            try:
                notifier.send(notification)
            except Exception as e:
                print(f"[WARN] Falló canal {notifier.__class__.__name__}: {e}")


# =========================
# Demo
# =========================
def demo() -> None:
    # Intercambiable: mismo servicio, cambia el canal por inyección
    email_service = NotificationService(EmailNotifier())
    sms_service = NotificationService(SMSNotifier())
    push_service = NotificationService(PushNotifier())
    slack_service = NotificationService(SlackNotifier())

    email_service.notify("david@email.com", "Bienvenido", "Tu cuenta fue creada.")
    push_service.notify("device_token_123", "Oferta", "Tienes 20% de descuento.")
    slack_service.notify("#general", "Deploy", "Se desplegó la versión 1.2.0")

    # ¿Qué pasa si un canal falla? (SMS con número inválido)
    try:
        sms_service.notify("3001234567", "Código", "Tu código es 9999")
    except Exception as e:
        print("Canal falló:", e)

    # Multicanal: si uno falla, los demás siguen
    multi = MultiChannelNotificationService([
        EmailNotifier(),
        SMSNotifier(),
        PushNotifier(),
        SlackNotifier(),
    ])

    print("\n--- Envío multicanal con tolerancia a fallos ---")
    multi.notify_all("3001234567", "Alerta", "Esto prueba fallo en SMS pero continúan los demás.")


if __name__ == "__main__":
    demo()
