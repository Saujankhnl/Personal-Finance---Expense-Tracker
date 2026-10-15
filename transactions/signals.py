from django.contrib.auth import user_logged_in
from django.dispatch import receiver
from django.conf import settings

@receiver(user_logged_in)
def handle_remember_me(sender, request, user, **kwargs):
    # Check if the form had a "remember_me" field
    remember_me = request.POST.get('remember_me')
    
    if not remember_me:
        # Session expires when browser closes
        request.session.set_expiry(0)
    else:
        # Session lasts for SESSION_COOKIE_AGE (e.g., 30 days)
        request.session.set_expiry(settings.SESSION_COOKIE_AGE)