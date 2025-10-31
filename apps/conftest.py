import os
import django
import pytest
from rest_framework.test import APIClient
from apps.tests.factories import UsuarioFactory

# ------------------------------
# Configuración global de Django
# ------------------------------
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simulador_pytest.settings")
django.setup()

# ------------------------------
# Fixtures de cliente API
# ------------------------------


@pytest.fixture
def api_client(db):
    """
    Retorna un cliente DRF APIClient para tests de endpoints.
    Incluye 'db' para asegurar acceso a la base de datos de pruebas.
    """
    return APIClient()


# ------------------------------
# Fixtures de usuarios
# ------------------------------
@pytest.fixture
def usuario_factory(db):
    """
    Retorna una factory para crear usuarios flexibles.
    Uso: usuario_factory(is_active=False)
    """
    return UsuarioFactory


@pytest.fixture
def usuario_activo(usuario_factory):
    """Usuario activo por defecto"""
    return usuario_factory(is_active=True)


@pytest.fixture
def usuario_inactivo(usuario_factory):
    """Usuario inactivo por defecto"""
    return usuario_factory(is_active=False)
