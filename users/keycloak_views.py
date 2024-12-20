import requests
from django.contrib.auth import login
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User
# from .models import ServiceUser
from urllib.parse import urlencode

from pprint import pprint

def keycloak_login(request):
    keycloak_url = f"{settings.KEYCLOAK_SERVER_URL}realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/auth"
    params = {
        "client_id": settings.KEYCLOAK_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": settings.KEYCLOAK_REDIRECT_URI,
        "scope": "openid email profile",
    }
    return redirect(f"{keycloak_url}?{urlencode(params)}")

def keycloak_callback(request):
    code = request.GET.get("code")
    if not code:
        return redirect("login")

    # Запрос токена
    token_url = f"{settings.KEYCLOAK_SERVER_URL}realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/token"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.KEYCLOAK_REDIRECT_URI,
        "client_id": settings.KEYCLOAK_CLIENT_ID,
        "client_secret": settings.KEYCLOAK_CLIENT_SECRET,
    }
    response = requests.post(token_url, data=data)
    if response.status_code != 200:
        return redirect("landing")

    tokens = response.json()
    access_token = tokens.get("access_token")

    # Декодирование JWT и создание пользователя
    user_info_url = f"{settings.KEYCLOAK_SERVER_URL}realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    user_info_response = requests.get(user_info_url, headers=headers)
    if user_info_response.status_code != 200:
        return redirect("users:profile")

    user_info = user_info_response.json()

    pprint(user_info)
    username = user_info.get("preferred_username")
    email = user_info.get("email")
    first_name = user_info.get("given_name")
    last_name = user_info.get("family_name")
    # phone = user_info.get("phone")

    # Создаем или получаем пользователя
    user, created = User.objects.get_or_create(username=username, defaults={
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        # "phone": phone
    })
    try:
        user.first_name = first_name
        user.last_name = last_name
        # user.phone = phone
        user.save()
    except:
        print('Fail save')
    login(request, user)
    return redirect("users:profile")

def keycloak_logout(request):
    logout_url = f"{settings.KEYCLOAK_SERVER_URL}realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/logout"
    params = {
        "redirect_uri": settings.KEYCLOAK_REDIRECT_URI,
    }
    return redirect(f"{logout_url}?{urlencode(params)}")

