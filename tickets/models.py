from django.db import models
import uuid
from django.contrib.auth.models import User

STATUS = (
    ('PENDING', 'Pending'),
    ("CLOSED", "Closed")
)


class Category(models.Model):
    name =models.CharField(max_length = 150)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    title = models.CharField(max_length=150, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(choices=STATUS, max_length=225, default='Pending')
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=225, blank=True, unique=True)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' - ' + self.ticket_id

def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1]

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" "))==0:
            self.ticket_id = generate_ticket_id()

        super(Ticket, self).save(*args, **kwargs)
    class Meta:
        ordering = ["-created"]


