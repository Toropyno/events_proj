from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from events.models import Event

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class EventSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='event-detail', read_only=True)

    class Meta:
        model = Event
        fields = (
            'url',
            'id',
            'title',
            'description',
            'date',
        )


class CreateEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'title',
            'description',
            'date',
            'creator',
        )
