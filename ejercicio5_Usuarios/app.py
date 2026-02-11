# app.py
from roles import (
    User,
    AdminRole,
    ClientRole,
    GuestRole,
    ModeratorRole,
    CanViewCatalog,
    CanManageUsers,
    CanPurchase,
)


# Casos de uso o Servicios 

def show_catalog(user: User) -> None:
    if isinstance(user.role, CanViewCatalog):
        user.role.view_catalog()
        return
    raise PermissionError(f"El rol '{user.role.name}' no puede ver el catálogo.")


def admin_create_user(actor: User, new_username: str) -> None:
    if isinstance(actor.role, CanManageUsers):
        actor.role.create_user(new_username)
        return
    raise PermissionError(f"El rol '{actor.role.name}' no puede crear usuarios.")


def admin_delete_user(actor: User, username_to_delete: str) -> None:
    if isinstance(actor.role, CanManageUsers):
        actor.role.delete_user(username_to_delete)
        return
    raise PermissionError(f"El rol '{actor.role.name}' no puede eliminar usuarios.")


def make_purchase(buyer: User, product_id: str, qty: int) -> None:
    if isinstance(buyer.role, CanPurchase):
        buyer.role.buy(product_id, qty)
        return
    raise PermissionError(f"El rol '{buyer.role.name}' no puede comprar.")


# Demo

def demo() -> None:
    admin = User("alice", AdminRole())
    client = User("bob", ClientRole())
    guest = User("carol", GuestRole())
    moderator = User("dave", ModeratorRole())

    # ---- Catálogo (todos pueden verlo) ----
    show_catalog(admin)
    show_catalog(client)
    show_catalog(guest)
    show_catalog(moderator)

    # ---- Acciones admin ----
    admin_create_user(admin, "nuevo_usuario")

    # ---- Compra (solo cliente) ----
    make_purchase(client, "P-001", 2)

    # ---- Invitado intenta comprar (debe fallar) ----
    try:
        make_purchase(guest, "P-002", 1)
    except PermissionError as e:
        print("Permiso denegado:", e)

    # ---- Moderador puede eliminar, pero no crear ----
    admin_delete_user(moderator, "spam_user")

    try:
        admin_create_user(moderator, "otro_user")
    except PermissionError as e:
        print("Permiso denegado:", e)

    # ---- Moderador intenta comprar (debe fallar) ----
    try:
        make_purchase(moderator, "P-999", 1)
    except PermissionError as e:
        print("Permiso denegado:", e)



if __name__ == "__main__":
    demo()
