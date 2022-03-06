
from django.urls import path, include
from users.views import UserAPI


urlpatterns = [
    path('', UserAPI.as_view())
]
