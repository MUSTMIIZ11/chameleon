from django.db import models


# Create your models here.
class Map(models.Model):
    map_id = models.IntegerField()
    map_name = models.CharField(max_length=50)
    map_url = models.TextField(max_length=100)
    user_id = models.IntegerField()
    create_time = models.DateField()

    def __str__(self):
        return self.map_name
