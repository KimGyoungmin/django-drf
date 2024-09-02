from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    ## Article 리소스
    path("translate/", views.TranslateView.as_view(), name="translate"),
]

