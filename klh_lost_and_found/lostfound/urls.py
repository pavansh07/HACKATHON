# klh_lost_and_found/urls.py

from django.contrib import admin
from django.urls import path
from lostfound import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home will be login_required
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('items/', views.item_list, name='item_list'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/lost/', views.lost_items, name='lost_items'),
    path('items/found/', views.found_items, name='found_items'),
]
