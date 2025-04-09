from django.db import models
from django.contrib.auth.models import User
import random
import string

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=5, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = generate_short_code()
            while ShortenedURL.objects.filter(short_code=self.short_code).exists():
                self.short_code = generate_short_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.original_url} -> {self.short_code}'
