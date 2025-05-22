from django.urls import path
from .views import RoomListView, RoomDetailView

urlpatterns = [
    path("api/rooms/", RoomListView.as_view(), name="rooms"),
    path("api/rooms/<slug:slug>/", RoomDetailView.as_view(), name="room-detail"),
]
