from django.contrib.auth import get_user_model

from django_filters import rest_framework as filters
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import CreateUserSerializer, EventSerializer, CreateEventSerializer
from . import filters as my_filters
from ..models import Event

User = get_user_model()


class CreateUserViewSet(mixins.CreateModelMixin,
                        GenericViewSet):
    """
    Регистрация пользователей
    """
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class EventViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = my_filters.EventFilter

    def get_queryset(self):
        return Event.objects.filter(creator=self.request.user)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['creator'] = request.user.id
        serializer = CreateEventSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
