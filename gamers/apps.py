from django.apps import AppConfig

class gamersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gamers'

    def ready(self):
        import gamers.signals

