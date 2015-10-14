from rest_framework.generics import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from web.configurations.serializers.configuration_serializer import ConfigurationSerializer


class NewConfigurationViewSet(mixins.CreateModelMixin, GenericViewSet):

    serializer_class = ConfigurationSerializer
    permission_classes = (AllowAny,)