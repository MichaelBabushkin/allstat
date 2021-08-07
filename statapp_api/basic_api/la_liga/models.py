from django.db import models
#  country, name, logo, short_code

class laLigaTeams(models.Model):
    name = models.CharField("Name", max_length=240)
    country = models.CharField("Country",default="Spain", max_length=20)
    shortCode = models.CharField("Short Code", max_length=10)
    logo = models.URLField("Logo", max_length=240)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name