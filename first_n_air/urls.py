from django.urls import path

from first_n_air.views import home
from .views import contact, product, register, single

urlpatterns =[
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("product/<slug>/", product, name="product"),
    path("register/", register, name="register"),
    path("single/<int:pk>/", single, name="single"),
]