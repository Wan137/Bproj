from rest_framework import serializers
from ..models import Teacher
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('phone_number', 'password', 'class_name', 'subject_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        teacher = Teacher(
            phone_number=validated_data['phone_number'],
            class_name=validated_data['class_name'],
            subject_name=validated_data['subject_name'],
        )
        teacher.set_password(validated_data['password'])
        teacher.save()
        return teacher

class TeacherLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['phone_number'] = user.phone_number
        return token