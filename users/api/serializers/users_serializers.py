from rest_framework import serializers
from users.models import User


class UserTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)


class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'quota',
            'date_joined',
            'last_login',
            'is_admin',
            'is_active',
            'is_staff',
            'is_superuser',
        )

    def to_representation(self,instance):
        return {
            'id': instance.id,
            'email': instance.email,
            'quota': instance.quota.max_resources,
            'date_joined': instance.date_joined,
            'last_login': instance.last_login,
            'is_admin': instance.is_admin,
            'is_active': instance.is_active,
            'is_staff': instance.is_staff,
            'is_superuser': instance.is_superuser
        }


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )

    def validate(self, attrs):
        # Validate if email is in use.
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        
        return super().validate(attrs)

    def create(self, validated_data):

        email = validated_data.get('email', '')
        password = validated_data.get('password', '')

        user = User.objects.create_user(username=email, email=email)
        user.set_password(password)
        user.save()

        return user
