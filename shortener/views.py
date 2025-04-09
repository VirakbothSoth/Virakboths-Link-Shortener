from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.utils import timezone
from django.http import HttpResponseNotFound
from django.conf import settings
from django.shortcuts import render
import random
import string
import re
from .forms import URLForm
from .models import ShortenedURL


def validate_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, url) is None:
        raise ValidationError(f"Invalid URL: {url}")
    return url


@login_required
def shorten_url(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
            shortened_url = ShortenedURL(
                original_url=original_url,
                short_code=short_code,
                user=request.user
            )
            shortened_url.save()
            return redirect('user_links')
    else:
        form = URLForm()
    return render(request, 'shortener/index.html', {'form': form})


@login_required
def user_links(request):
    links = ShortenedURL.objects.filter(user=request.user)
    base_url = request.scheme + "://" + request.get_host()

    for link in links:
        time_left = link.expires_at - timezone.now()
        if time_left.total_seconds() < 0:
            link.is_expired = True
            link.time_left = "Expired"
        else:
            link.is_expired = False
            days_left = time_left.days
            hours_left = time_left.seconds // 3600
            minutes_left = (time_left.seconds % 3600) // 60

            if days_left > 0:
                link.time_left = f"{days_left} days left"
            elif hours_left > 0:
                link.time_left = f"{hours_left} hours left"
            elif minutes_left > 0:
                link.time_left = f"{minutes_left} minutes left"
            else:
                link.time_left = "Less than a minute left"

    return render(request, 'shortener/user_links.html', {'links': links, 'base_url': base_url})


def redirect_to_original(request, short_code):
    url_entry = get_object_or_404(ShortenedURL, short_code=short_code)
    if url_entry.expires_at and url_entry.expires_at < now():
        return HttpResponseNotFound("This shortened link has expired.")
    return redirect(url_entry.original_url)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("shorten_url")
    else:
        form = AuthenticationForm()
    return render(request, "shortener/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("shorten_url")


@login_required
def delete_link(request, short_code):
    try:
        link = ShortenedURL.objects.get(short_code=short_code, user=request.user)
        link.delete()
    except ShortenedURL.DoesNotExist:
        pass
    return redirect('user_links')


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_links')
    else:
        form = UserCreationForm()
    return render(request, 'shortener/signup.html', {'form': form})
