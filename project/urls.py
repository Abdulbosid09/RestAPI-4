from django.contrib import admin
from django.urls import path

from app.views import CategoryRetrieveUpdateDestroyAPIView, ProductRetrieveUpdateDestroyAPIView, ReviewRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product'),
    path('api/v1/category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category'),
    path('api/v1/review/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review'),
]