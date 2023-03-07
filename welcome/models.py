from django.db import models

class WelcomeText(models.Model):
    welcome_text = models.CharField(max_length=1500)
    def __str__(self):
        return str(self.welcome_text)
        

