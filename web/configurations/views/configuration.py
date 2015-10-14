from rest_framework.generics import mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from web.configurations.models import Configuration
from web.configurations.serializers.change_configuration_serializer import ChangeConfigurationSerializer
from web.constants import DOES_NOT_EXIST


class ConfigurationViewSet(mixins.UpdateModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):

    serializer_class = ChangeConfigurationSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        client_id = self.request.query_params.get('client_id')
        return Configuration.objects.filter(client_id=client_id)

    def update(self, request, *args, **kwargs):
        client_id = self.request.query_params.get('client_id')
        config_queryset = Configuration.objects.filter(client_id=client_id)
        if config_queryset.exists():
            instance = config_queryset[0]
            partial = kwargs.pop('partial', False)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response = Response(serializer.data)
        else:
            response = Response(DOES_NOT_EXIST)
        return response