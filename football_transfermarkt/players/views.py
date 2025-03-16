from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import PlayerSerializer
from .models import Player


class PlayerDetailView(RetrieveUpdateAPIView):
    """API view for retrieving and updating details of a specific player."""

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
