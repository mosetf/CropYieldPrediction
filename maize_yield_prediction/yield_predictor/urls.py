from django.contrib import admin
from django.urls import include, path
from .views import predict_yield

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', predict_yield, name='predict_yield'),
]