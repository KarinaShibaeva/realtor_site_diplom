from django.urls import path
from flats.views import flat_list_view, flat_sell_view, flats_sale2_view

app_name = 'flats'

urlpatterns = [path("list/",flat_list_view, name="list"),
               path("sell/", flat_sell_view, name="sell"),
               path("", flats_sale2_view, name="sale_two")
               ]

