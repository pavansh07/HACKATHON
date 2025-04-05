# klh_lost_and_found/urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from lostfound import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('items/', views.item_list, name='item_list'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/lost/', views.lost_items, name='lost_items'),
    path('items/found/', views.found_items, name='found_items'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('chatbot-ui/', views.chatbot_page, name='chatbot'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)