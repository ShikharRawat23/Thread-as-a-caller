import threading
from django.http import HttpResponse
from django.contrib.auth.models import User


def create_user(request):
    print(f"[VIEW] Running in Thread ID: {threading.get_ident()}")

   
    User.objects.create(username="test_user_signal")

    return HttpResponse("User created, check console for thread IDs")
