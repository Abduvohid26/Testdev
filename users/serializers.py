from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, PaperInformation

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'affiliation', 'country', 'password']

    
    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, attrs):
        email = attrs.get('email')

        if email and User.objects.filter(email=email).exists():
            return ValidationError(
                {
                    'email': 'Email already exists'
                }
            )
        return attrs
    


class AddYourSelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'affiliation', 'country']

    
class PaperInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperInformation
        fields = ['id', 'title', 'key_words', 'section', 'file']