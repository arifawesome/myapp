from django.conf import settings




LOGIN_REDIRECT_URL = getattr(settings, 'LOGIN_REDIRECT_URL', '/')

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
USERINFO_MODEL=getattr(settings, 'USER_INFO_MODEL', 'user.UserInfo')