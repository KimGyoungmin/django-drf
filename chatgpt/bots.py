from django.conf import settings
from openai import OpenAI

CLIENT = OpenAI(
    api_key=settings.OPENAI_API_KEY,
)


def django_bot(user_message):
    system_instructions = """
    너는 이제부터 Django 프레임워크에 대해 설명하고
    사용자가 Django 프레임워크에 대해 어려움을 겪고 있다고 가정하고 도와주는 챗봇이 되어야해.
    다른 코딩 언어나 프레임워크에 대해 설명하거나 다른 주제로 이야기하는 것은 금지야.
    Django 공식문서의 링크를 제공하거나 Django 프레임워크에 대한 설명도 추가해줘.
    """
    completion = CLIENT.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_instructions,
            },
            {
                "role": "user",
                "content": user_message,
            }
        ],
    )
    return completion.choices[0].message.content
