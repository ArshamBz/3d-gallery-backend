from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import Room
from .serializers import RoomSerializer, RoomListSerializer


class RoomListView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer

class RoomDetailView(RetrieveAPIView):
    queryset = Room.objects.prefetch_related("images").all()
    serializer_class = RoomSerializer
    lookup_field = "slug"
