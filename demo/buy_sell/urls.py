from django.urls import path, include

from buy_sell import views

urlpatterns = [
    path("", views.index, name="buy_sell_index"),
]