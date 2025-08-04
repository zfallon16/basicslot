from django.urls import path
from .views import play, signup, logout_every_which_way

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', logout_every_which_way, name='logout'),
    path('', play, name='play'),
]