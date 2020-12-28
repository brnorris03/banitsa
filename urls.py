from django.contrib import admin
from django.urls import include, path

from .banitsa import views

urlpatterns = [
    path(r'banitsa/', include('banitsa.urls', namespace="banitsa")),
    path(r'admin/', admin.site.urls),
    path(r'pick/', views.pick, name='pick'),
]