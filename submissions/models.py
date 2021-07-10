from django.db import models

# Submissions model
class Submission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('auth.User', related_name='submissions', on_delete=models.DO_NOTHING)
    link = models.URLField(
        max_length=128,
        unique=True,
        blank=False,
    )
    assignment = models.ForeignKey(
        'assignments.Assignment',
        related_name='submissions',
        on_delete=models.DO_NOTHING,
    )


    class Meta:
        ordering = ['created']