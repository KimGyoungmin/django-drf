from rest_framework.views import APIView
from openai import OpenAI
from django.conf import settings
from rest_framework.response import Response
from .bots import django_bot

class TranslateView(APIView):
    def post(self, request):
        user_message = request.data.get("message")
        chatgpt_response = django_bot(user_message)
        return Response({"message": chatgpt_response})
