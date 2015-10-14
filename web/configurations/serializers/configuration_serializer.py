from rest_framework import serializers
from web.configurations.models import Configuration


class ConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Configuration
        fields = ('id', 'client_id', 'configured_url')

    def create(self, validated_data):
        client_id = validated_data.pop('client_id')
        configured_url=validated_data.pop('configured_url')
        config = Configuration.objects.create_configuration(client_id=client_id, configured_url=configured_url)
        config.save()
        return config
