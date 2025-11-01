from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path("api/", lambda: HttpResponse(include("apps.usuarios.urls"))),
    path("", lambda request: HttpResponse("Hola mundo")),
    path("admin/", admin.site.urls)
]
