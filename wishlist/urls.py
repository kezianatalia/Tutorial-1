from django.urls import path
from wishlist.views import show_wishlist, show_wishlist_ajax
from wishlist.views import show_xml 
from wishlist.views import show_json
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user
from wishlist.views import create_wishlist
from wishlist.views import show_ajax

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_ajax, name='show_wishlist_ajax'),
    path('ajax/submit', create_wishlist, name='create_wishlist'),
]