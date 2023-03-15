from rest_framework import serializers

from textbook.models import BookTag, Textbook, Syllabus, Course
from user_info.serializers import UserDescSerializer


class BookTagSerializer(serializers.ModelSerializer):

    def check_tag_obj_exists(self, validated_data):
        text = validated_data.get('text')
        if BookTag.objects.filter(text=text).exists():
            raise serializers.ValidationError('Tag with text {} exists.'.format(text))

    def create(self, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().update(instance, validated_data)

    class Meta:
        model = BookTag
        fields = '__all__'


class TextbookSerializer(serializers.ModelSerializer):
    uploader = UserDescSerializer(read_only=True)
    tags = serializers.SlugRelatedField(
        queryset=BookTag.objects.all(),
        many=True,
        required=False,
        slug_field='text'
    )

    class Meta:
        model = Textbook
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='course-detail')
    textbooks = TextbookSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = '__all__'


class SyllabusSerializer(serializers.ModelSerializer):
    uploader = UserDescSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Syllabus
        fields = '__all__'
