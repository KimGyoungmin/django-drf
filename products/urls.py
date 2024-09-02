from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    ## Product 리소스
    path("", views.ProductListAPIView.as_view(), name="products_list"),

]

