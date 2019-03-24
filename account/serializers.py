from rest_framework import serializers

from .models import *



class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        # fields = ('username', 'email')
        fields = '__all__'
        # for returning all values

class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = '__all__'


class categoryinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DocumentationSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=True, read_only=True, slug_field='new_category', allow_null=True)

    class Meta:
        model = Documentation
        fields = '__all__'


class userpullSerializer(serializers.ModelSerializer):

    class Meta:
        model = user
        fields = ('username',)


class ForumQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form_question
        fields = ("user", "question", 'date')
