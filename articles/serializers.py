from .models import Article, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        # 쓰기 요청할때 건들지 말라는 필드 작성
        read_only_fields = ("article",)
    
    ## articleid값은 브라우저상에서는 필요없기때문에 serializer에 custom기능을 사용할수있다.
    ## serialization한 값들을 가져온다
    def to_representation(self, instance):
        ## ret는 원래 기존의 json형식의 값
        ret = super().to_representation(instance)
        ## ret라는 변수에 값을 넣어주고 필요없는 article값을 없애준다
        ret.pop("article")
        return ret

## 모든 게시글의 대한 직렬클래스  -> 여기선 댓글들의 대한 데이터가 없다
class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = "__all__"

## 모든 게시글 직렬클래스를 상속받은 디테일 클래스        
class ArticleDetailSerializer(ArticleSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(
        source="comments.count", read_only=True)