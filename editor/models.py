from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=10)
    piston_lang = models.CharField(max_length=10)
    editor_lang = models.CharField(max_length=10)
    demo_code = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.language