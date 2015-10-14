from django.db import models
from django.core.validators import URLValidator, EmailValidator
from django.utils import timezone


class ConfigurationManager(models.Manager):

    def create_configuration(self, client_id, configured_url):
        config = self.model(client_id=client_id, configured_url=configured_url)
        config.save(using=self._db)
        return config


class Configuration(models.Model):
    client_id = models.EmailField(validators=[EmailValidator()], unique=True)
    configured_url = models.TextField(validators=[URLValidator()], max_length=2000)
    is_active = models.BooleanField(default=True)
    configured_on = models.DateTimeField(default=timezone.now)

    objects = ConfigurationManager()