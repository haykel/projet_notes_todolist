from django.db import models

class Todo(models.Model):
    """
    Task entity.
    """

    class Status(models.TextChoices):
        TODO = "todo", "To do"
        IN_PROGRESS = "in_progress", "In progress"
        DONE = "done", "Done"

    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
