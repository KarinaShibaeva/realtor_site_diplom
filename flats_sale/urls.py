from django.urls import path

from flats_sale.views import SaleListView, sale_id_view

app_name = "flats_sale"
urlpatterns = [
    path('sale/', SaleListView.as_view(), name = "sale"),
    path("sale/<int:pk>/", sale_id_view,  name="flat"),
]