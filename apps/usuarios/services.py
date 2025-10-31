def send_email(email: str, mensaje: str):
    """Simula envío de correo"""
    print(f"Enviando email a {email}: {mensaje}")
    return True


def notificar_usuario(usuario):
    """Notifica un usuario activo"""
    if not usuario.is_active:
        return "Usuario inactivo"
    send_email(usuario.email, "Bienvenido")
    return "Éxito"


def servicio_externo(usuario_id):
    """Simula un servicio externo"""
    return "ok"


def procesar_usuario(usuario_id):
    try:
        resultado = servicio_externo(usuario_id)
        return resultado
    except Exception:
        return "Fallo"
