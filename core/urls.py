from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/z8xjHEvOeDjAwW5ueSEW/', admin.site.urls),
    path('moisture_data/api/', include('moisture_data.api.urls'))
]
