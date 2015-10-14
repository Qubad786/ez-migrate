from django.utils import timezone
from rest_framework import serializers
from web.configurations.models import Configuration


class ChangeConfigurationSerializer(serializers.ModelSerializer):

    client_id = serializers.EmailField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    configured_on = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Configuration
        fields = ('id', 'client_id', 'configured_url', 'is_active', 'configured_on')

    def update(self, instance, validated_data):
        instance.configured_url = validated_data.get('configured_url', instance.configured_url)
        instance.configured_on = timezone.now()
        instance.save()
        return instance
