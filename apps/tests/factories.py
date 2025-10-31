import factory
from apps.usuarios.models import Usuario


class UsuarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Usuario

    email = factory.Faker("email")
    password = "testpass"
    is_active = True
