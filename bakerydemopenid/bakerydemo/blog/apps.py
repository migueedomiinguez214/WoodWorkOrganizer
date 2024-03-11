from django.apps import AppConfig

class Blogconfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bakerydemo.blog'
    def ready(self):
        import bakerydemo.blog.signals
