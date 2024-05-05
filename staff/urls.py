from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from staff.views import staff_view

app_name = "staff"
urlpatterns = [
    path('', staff_view, name = "staf"),
]

if settings.DEBUG:
     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
