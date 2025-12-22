from django.db import models

class Note(models.Model):
    """
    Textual note that can be linked to multiple todos.
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
