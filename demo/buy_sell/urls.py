from django.urls import path, include

from buy_sell import views

urlpatterns = [
    path("", views.index, name="buy_sell_index"),
    path("/create", views.create_listing, name="buy_sell_create"),
    path("/view/<int:ad_id>", views.view_listing, name="buy_sell_view"),
]