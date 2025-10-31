# apps/usuarios/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.usuarios.models import Usuario
from apps.usuarios.serializers import UsuarioSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email y password requeridos"}, status=400)

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=404)

        if usuario.password != password:
            return Response({"error": "Password incorrecto"}, status=401)

        serializer = UsuarioSerializer(usuario)
        return Response({"token": "dummy-token", "usuario": serializer.data})


class UsuarioView(APIView):
    """Endpoints para CRUD de usuarios"""

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response({"usuario": UsuarioSerializer(usuario).data}, status=201)
        return Response({"errores": serializer.errors}, status=400)

    def put(self, request, usuario_id):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=404)

        serializer = UsuarioSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response({"usuario": UsuarioSerializer(usuario).data})
        return Response({"errores": serializer.errors}, status=400)

    def delete(self, request, usuario_id):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=404)

        usuario.delete()
        return Response({"mensaje": "Usuario eliminado"}, status=200)
