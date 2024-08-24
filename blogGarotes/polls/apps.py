from django.apps import AppConfig

# Essa classe é criada para poder adicionar a configuração do aplicativo polls, feita dentro do arquivo polls/models.py
# dentro do arquivo blogGarotes/settings.py.
class PollsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"
