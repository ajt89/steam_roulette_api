from django.db import models


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SteamApp(BaseModel):
    appid = models.IntegerField()
    name = models.CharField(max_length=255, unique=False)
