from django.db import models


class Fruits(models.Model):
    fruit_name = models.CharField(max_length=100)
    price = models.IntegerField()
    manufacture_date = models.DateField()
    fruits_description = models.TextField()
    is_fresh = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.fruit_name
    
    class Meta:
        db_table = 'home_fruits'
        verbose_name = 'home_fruits'
        ordering = ['-fruit_name']