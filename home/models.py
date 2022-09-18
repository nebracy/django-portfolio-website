from django.db import models


class Commit(models.Model):
    commit_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    url = models.URLField()
    date = models.DateTimeField()
    msg = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.commit_id
