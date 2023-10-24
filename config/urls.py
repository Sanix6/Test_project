from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as yasg_url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("src.account.urls"))
]

urlpatterns += yasg_url