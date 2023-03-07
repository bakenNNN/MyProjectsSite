from django.db import models

class InnerText(models.Model):
    ProjectText = models.CharField(max_length=999999999)
    def __str__(self):
        return str(self.ProjectText)
class TitleText(models.Model):
    HeaderText= models.CharField(max_length=1500)
    def __str__(self):
        return str(self.HeaderText)
