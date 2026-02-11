# roles.py
from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod


# ========== Interfaces (ISP) ==========

class UserRole(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...


class CanManageUsers(ABC):
    @abstractmethod
    def create_user(self, username: str) -> None: ...

    @abstractmethod
    def delete_user(self, username: str) -> None: ...


class CanPurchase(ABC):
    @abstractmethod
    def buy(self, product_id: str, qty: int) -> None: ...


class CanViewCatalog(ABC):
    @abstractmethod
    def view_catalog(self) -> None: ...


# ========== Roles (OCP) ==========

class AdminRole(UserRole, CanManageUsers, CanViewCatalog):
    @property
    def name(self) -> str:
        return "admin"

    def create_user(self, username: str) -> None:
        print(f"[Admin] Usuario '{username}' creado.")

    def delete_user(self, username: str) -> None:
        print(f"[Admin] Usuario '{username}' eliminado.")

    def view_catalog(self) -> None:
        print("[Admin] Mostrando catálogo completo.")


class ClientRole(UserRole, CanPurchase, CanViewCatalog):
    @property
    def name(self) -> str:
        return "cliente"

    def buy(self, product_id: str, qty: int) -> None:
        print(f"[Cliente] Compró {qty} unidad(es) del producto '{product_id}'.")

    def view_catalog(self) -> None:
        print("[Cliente] Mostrando catálogo público.")


class GuestRole(UserRole, CanViewCatalog):
    @property
    def name(self) -> str:
        return "invitado"

    def view_catalog(self) -> None:
        print("[Invitado] Mostrando catálogo limitado.")

class ModeratorRole(UserRole, CanManageUsers, CanViewCatalog):
    @property
    def name(self) -> str:
        return "moderador"

    def create_user(self, username: str) -> None:
        raise PermissionError("[Moderador] No puede crear usuarios.")

    def delete_user(self, username: str) -> None:
        print(f"[Moderador] Usuario '{username}' eliminado.")

    def view_catalog(self) -> None:
        print("[Moderador] Mostrando catálogo (modo moderación).")


# ========== Modelo (composición class user) ==========

@dataclass(frozen=True)
class User:
    username: str
    role: UserRole
