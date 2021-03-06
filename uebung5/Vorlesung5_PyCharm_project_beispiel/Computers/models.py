from django.db import models
from django.contrib.auth.models import User


class Computer(models.Model):
    BRANDS = [
        ('A', 'Apple'),
        ('H', 'HP'),
        ('M', 'Microsoft'),
        ('S', 'Sony'),
    ]

    TYPES = [
        ('D', 'Desktop'),
        ('L', 'Laptop'),
        ('N', 'Netbook'),
    ]

    OPERATING_SYSTEMS = [
        ('L', 'Linux'),
        ('M', 'MacOS'),
        ('W', 'Windows'),
    ]

    brand = models.CharField(max_length=1,
                            choices=BRANDS,
                            )
    type = models.CharField(max_length=1,
                            choices=TYPES,
                            )
    operating_system = models.CharField(max_length=1,
                            choices=OPERATING_SYSTEMS,
                            )
    memory = models.IntegerField()  # Must call function to take effect
    serial_number = models.CharField(max_length=50)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='computer_created_by',
                             related_query_name='computer_created_by',
                             )

    class Meta:
        ordering = ['type', 'brand', 'serial_number']
        verbose_name = 'Computer'
        verbose_name_plural = 'Computers'

    def __str__(self):
        return self.get_brand_display() + ' / ' + self.get_type_display()

    def __repr__(self):
        return self.get_brand_display() + ' / ' + self.get_type_display() + ' / ' + self.get_operating_system_display() + ' / ' + str(self.memory) + ' Gb'
