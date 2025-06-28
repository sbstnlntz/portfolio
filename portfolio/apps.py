from django.apps import AppConfig

class PortfolioConfig(AppConfig):
    """
    Configuration class for the 'portfolio' Django app.

    - Sets the default auto field type for model primary keys.
    - Automatically loads translation registration on app startup.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'

    def ready(self):
        """
        Called when the app is ready.
        Ensures that model translation definitions are loaded.
        """
        import portfolio.translation
