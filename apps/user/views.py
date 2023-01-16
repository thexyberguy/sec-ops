import json
import os
import pickle
from dataclasses import dataclass
import base64

from django.http import HttpResponse, JsonResponse
from django.utils.safestring import mark_safe

from apps.user.models import User


def get_users(request, user_id):

    users = User.objects.raw(f'SELECT * FROM security_user WHERE id = {user_id}')

    return HttpResponse(users)




def log(request):
    string = request.GET.get('string', '')
    return HttpResponse(string)
