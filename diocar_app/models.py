from django.db import models

# define the class Person
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_id = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

