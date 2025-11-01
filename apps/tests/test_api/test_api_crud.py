import pytest


@pytest.mark.django_db
def test_crear_usuario(api_client):
    data = {"email": "nuevo@user.com", "is_active": True}
    response = api_client.post("/api/usuarios/", data)
    assert response.status_code == 201
    assert response.data["usuario"]["email"] == data["email"]


@pytest.mark.django_db
def test_usuario_str(usuario_activo):
    """Verifica que __str__ retorna el email del usuario"""
    assert str(usuario_activo) == usuario_activo.email


@pytest.mark.django_db
def test_login_sin_email_o_password(api_client):
    # Enviar request vacío
    response = api_client.post("/api/login/", {})
    assert response.status_code == 400
    assert response.data["error"] == "Email y password requeridos"


@pytest.mark.django_db
def test_crear_usuario_fail(api_client):
    data = {"is_active": True}
    response = api_client.post("/api/usuarios/", data)
    assert response.status_code == 400
    assert 'email' in response.data['errores']


@pytest.mark.django_db
def test_actualizar_usuario(api_client, usuario_activo):
    response = api_client.put(f"/api/usuarios/{usuario_activo.id}/", {"is_active": False})
    assert response.status_code == 200
    assert response.data["usuario"]["is_active"] is False


@pytest.mark.django_db
def test_actualizar_usuario_fail_404(api_client, usuario_activo):
    response = api_client.put("/api/usuarios/99999/", {"email": 'test@outlook.com', "is_active": True})
    assert response.status_code == 404
    assert response.data['error'] == 'Usuario no encontrado'


@pytest.mark.django_db
def test_eliminar_usuario(api_client, usuario_activo):
    response = api_client.delete(f"/api/usuarios/{usuario_activo.id}/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_eliminar_usuario_fail(api_client, usuario_activo):
    response = api_client.delete("/api/usuarios/9999/")
    assert response.status_code == 404
    assert response.data['error'] == 'Usuario no encontrado'


@pytest.mark.django_db
def test_login_exitoso(api_client, usuario_activo):
    response = api_client.post("/api/login/", {"email": usuario_activo.email, "password": "testpass"})
    assert response.status_code == 200
    assert "token" in response.data


@pytest.mark.django_db
def test_login_incorrecto(api_client, usuario_activo):
    response = api_client.post("/api/login/", {"email": usuario_activo.email, "password": "wrong"})
    assert response.status_code == 401


@pytest.mark.django_db
def test_login_usuario_no_existente(api_client):
    response = api_client.post("/api/login/", {"email": "no@existe.com", "password": "test"})
    assert response.status_code == 404
