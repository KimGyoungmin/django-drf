from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from django.http import JsonResponse, HttpResponse
from drf_spectacular.utils import extend_schema
from django.core import serializers
from rest_framework.decorators import api_view
from .serializers import (
    ArticleSerializer, ArticleDetailSerializer, CommentSerializer)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# FBV 방식
# @api_view(["GET", "POST"])
# def article_list(request):
#     if request.method == "GET":
#         articles= Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         # data = request.data
#         # title = data.get("title")
#         # content = data.get("content")
#         # article = Article.objects.create(title = title, content = content)
#         # return Response({})
#         serializer = ArticleSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):  ## raise_exception을 True로 넣어주면 알아서 예외처리를 해준다
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return Response(serializer.errors, status = 400) ## raise_exception을 안써주면 작성

# @api_view(["GET","DELETE","PUT"])
# def article_detail(request, pk):

#     article = get_object_or_404(Article, pk = pk)
#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

# CBV 방식
class ArticleListAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    @extend_schema(
        tags=["Articles"],
        description="Article 목록 조회를 위한 API",
    )
    # 전체리스트조회, 리스트 생성
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @extend_schema(
        tags=["Articles"],
        description="Article 생성을 위한 API",
        request=ArticleSerializer,
    )
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        # raise_exception을 True로 넣어주면 알아서 예외처리를 해준다
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailAPIView(APIView):
    permission_classes = [
        IsAuthenticated
    ]
    # 특정 object 리턴 함수

    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)
    # 특정 object 조회

    def get(self, request, pk):
        user = request.user
        article = self.get_object(pk=pk)
        serializers = ArticleDetailSerializer(article)
        return Response(serializers.data)

    # 특정 object 수정
    def put(self, request, pk):
        article = self.get_object(pk=pk)
        serializers = ArticleDetailSerializer(
            article, data=request.data, partial=True)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)

    # 특정 object 삭제
    def delete(self, request, pk):
        article = self.get_object(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Generic views를 사용하여 간단한 CRUD구현 // urls는 apiview와 동일
# from rest_framework import generics

# class ArticleListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# viewset을 사용하여 간단한 crud 구현 // urls는 다름
# from rest_framework import viewsets

# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


class CommentListAPIView(APIView):
    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        comments = article.comments.all()
        # article.comment_set.all()   -> 역참조할때 related_name을 설정안했을시 _set으로 접근
        # comments = Comment.objects.filter(article_pk = article_pk) -> 정참조일때는 필터사용
        serializers = CommentSerializer(comments, many=True)
        return Response(serializers.data)

    def post(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentDetailAPIView(APIView):
    permission_classes = [
        IsAuthenticated
    ]

    def get_object(self, comment_pk):
        return get_object_or_404(Comment, comment_pk)

    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        serializer = CommentSerializer(
            comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
