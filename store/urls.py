from django.contrib import admin
from django.urls import path
from backend_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductsView.as_view(), name='govno'),
]
