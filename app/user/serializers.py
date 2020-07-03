from django.contrib.auth import get_user_model,authenticate
from django.utils.translation import ugettext as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User Object serializer"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create new user with encryption"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """update the user and setting the password"""
        password = validated_data.pop('password',None)
        user = super().update(instance,validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serialize for user authentication"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self,attrs):
        """Validate and authenticate"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to autherize with provided credentials')
            raise serializers.ValidationError(msg,code='authentication')
        attrs['user'] = user
        return attrs