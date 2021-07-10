from django.db import models

# Assignment model
class Assignment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('auth.User', related_name='assignments', on_delete=models.DO_NOTHING)
    description = models.TextField()
    group = models.ForeignKey('auth.Group', related_name='assignments', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, blank=False, default='')


    class Meta:
        ordering = ['created']
