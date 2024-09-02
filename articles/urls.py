from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    ## Article 리소스
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view(), name="article_detail"),
    ## Comment 리소스
    path("<int:article_pk>/comments/", views.CommentListAPIView.as_view(), name="comment_list"),
    path("comments/<int:comment_pk>/", views.CommentDetailAPIView.as_view(), name="comment_detail"),
]

## viewset을 사용할때
# from rest_framework.routers import DefaultRouter
# from .views import ArticleViewSet

# router = DefaultRouter()
# router.register(r'articles', ArticleViewSet)

# urlpatterns = [
#     ...
#     path('', include(router.urls)),
# ]
