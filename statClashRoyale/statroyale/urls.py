from django.urls import path
from .views import *

urlpatterns = [
    path('', show_main_page, name='main_page'),
    path('profile-statistics/<str:tag>/', GetProfileStatistics.as_view(), name='profile-statistics'),
]