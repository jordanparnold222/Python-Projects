from django.db import models

# Create your models here.

# The model that holds class information


class djangoClasses(models.Model):
    Title = models.CharField(max_length=40)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=25)
    Duration = models.FloatField()




# Allows the title of the class to be displayd in the admin panel
    def __str__(self):
        return self.Title

