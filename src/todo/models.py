from django.db import models



class Todo(models.Model):
    title   = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)


    class Meta:
        verbose_name        = "To Do"
        verbose_name_plural = "To Do's"
        ordering = ('id',)