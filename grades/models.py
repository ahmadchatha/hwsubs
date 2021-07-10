from django.db import models

# Grades model
class Grade(models.Model):
    GRADE_CHOICES = [
        ('A', 'a'),
        ('B', 'b'),
        ('C', 'c'),
        ('D', 'd'),
        ('E', 'e'),
        ('F', 'Fail'),
        ('I', 'Incomplete')
    ]
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('auth.User', related_name='grades', on_delete=models.DO_NOTHING)
    notes = models.TextField()
    final_grade = models.CharField(
        max_length=2,
        choices=GRADE_CHOICES,
        blank=False,
    )
    submission = models.OneToOneField(
        'submissions.Submission',
        on_delete=models.DO_NOTHING,
        primary_key=True,
    )


    class Meta:
        ordering = ['created']
