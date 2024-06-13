from django.urls import path
from AppsDePag import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("template1/<str:nombre>/<str:apellido>/<int:edad>", views.template1),
    path("template2/<str:nombre>/<str:apellido>/<int:edad>", views.template2),
    path("template3/<str:nombre>/<str:apellido>/<int:edad>", views.template3),
    path("probar/<str:nombre>/<str:apellido>/<int:edad>", views.template4, name="Prueba2"),
    path("probando/", views.probando),
    path("creacion/creacion/<str:modelo>/<str:marca>", views.creacion_de_mother, name="crear"),
    
]

