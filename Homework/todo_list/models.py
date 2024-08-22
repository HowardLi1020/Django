from django.db import models
from datetime import datetime
# Create your models here.
class toDoList(models.Model):
    todo_id = models.AutoField(primary_key=True)
    completed = models.BooleanField(default=False)
    todo = models.CharField(max_length=50)
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'todo_list'