from django.db import models

# Create your models here.

# The ORM allows how to create classes that 
# correspond to database tables. Class attributes
# correspond to columns. 
# and and instances correspond to rows. 

# Here we create a table with title, description and 
# technology. The table is called Projects
class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    technology = models.CharField(max_length = 20)
    
