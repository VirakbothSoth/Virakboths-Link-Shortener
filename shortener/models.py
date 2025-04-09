from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils.timezone import now
import random
import string

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=5, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def default_expiration():
        return now() + timedelta(days=5)

    expires_at = models.DateTimeField(default=default_expiration)

    def days_left(self):
        """Returns remaining days before expiration."""
        remaining = (self.expires_at - now()).days
        return max(remaining, 0)  # Ensure non-negative days

    def get_full_short_url(self, request=None):
        """Returns full domain + short code."""
        if request:
            domain = request.get_host()  # Safer way to get the domain
        else:
            domain = "http://127.0.0.1:8000"  # Fallback for local testing

        return f"{domain}/{self.short_code}"


    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = generate_short_code()
            while ShortenedURL.objects.filter(short_code=self.short_code).exists():
                self.short_code = generate_short_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.original_url} -> {self.short_code}'
