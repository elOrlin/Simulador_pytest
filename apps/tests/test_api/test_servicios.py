import pytest
from apps.usuarios import services


@pytest.mark.django_db
def test_send_email(mocker):
    """Verifica que send_email retorna True y simula el envío."""
    mock_print = mocker.patch("builtins.print")
    resultado = services.send_email("test@example.com", "Hola")
    mock_print.assert_called_once_with("Enviando email a test@example.com: Hola")
    assert resultado is True


@pytest.mark.django_db
def test_notificar_usuario_activo(mocker, usuario_activo):
    """Usuario activo envía email y retorna 'Éxito'."""
    mock_send = mocker.patch("apps.usuarios.services.send_email", return_value=True)
    resultado = services.notificar_usuario(usuario_activo)
    assert resultado == "Éxito"
    mock_send.assert_called_once_with(usuario_activo.email, "Bienvenido")


@pytest.mark.django_db
def test_notificar_usuario_inactivo(usuario_inactivo):
    """Usuario inactivo retorna 'Usuario inactivo' sin enviar email."""
    resultado = services.notificar_usuario(usuario_inactivo)
    assert resultado == "Usuario inactivo"


@pytest.mark.django_db
def test_servicio_externo():
    """Servicio externo siempre retorna 'ok'."""
    resultado = services.servicio_externo(1)
    assert resultado == "ok"


@pytest.mark.django_db
def test_procesar_usuario_exito(mocker, usuario_activo):
    """Procesar usuario retorna 'ok' si servicio_externo funciona."""
    mock_serv = mocker.patch("apps.usuarios.services.servicio_externo", return_value="ok")
    resultado = services.procesar_usuario(usuario_activo.id)
    assert resultado == "ok"
    mock_serv.assert_called_once_with(usuario_activo.id)


@pytest.mark.django_db
def test_procesar_usuario_fallo(mocker, usuario_activo):
    """Procesar usuario retorna 'Fallo' si servicio_externo lanza excepción."""
    mock_serv = mocker.patch("apps.usuarios.services.servicio_externo", side_effect=Exception("Error simulado"))
    resultado = services.procesar_usuario(usuario_activo.id)
    assert resultado == "Fallo"
    mock_serv.assert_called_once_with(usuario_activo.id)
