from django.urls import path
from bands import views

urlpatterns = [
    path('musician/<int:musician_id>/', views.musician, name='musician'),
    path('musicians/', views.musicians, name='musicians'),
    path('rooms/', views.room_list, name='room_list'),
    path('venues/<int:venue_id>/', views.venue_detail, name='venue_detail'),
]