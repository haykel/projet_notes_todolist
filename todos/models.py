from django.db import models


class Todo(models.Model):
    STATUS_CHOICES = (
        ("todo", "Todo"),
        ("done", "Done"),
    )

    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="todo",
    )
    note = models.ForeignKey(
        "notes.Note",
        on_delete=models.CASCADE,  # 🔥 SUPPRESSION EN CASCADE
        related_name="todos",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
