from django.apps import AppConfig


class GUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GUsers'
    
    def ready(self):
        import GUsers.signals
