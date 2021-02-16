from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
  path('', views.products_list_view, name='product-list'),
  path('<int:id>/', views.products_detail_view, name='product-detail')
]