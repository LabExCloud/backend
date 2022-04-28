from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=10, unique=True)
    piston_lang = models.CharField(max_length=10, unique=True)
    editor_lang = models.CharField(max_length=10, unique=True)
    demo_code = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.language