from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from .models import Team
from .serializers import TeamSerializer


class TeamListView(ListAPIView):
    """API view for retrieving a list of all teams."""

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetailView(RetrieveUpdateAPIView):
    """API view for retrieving and updating details of a specific team."""

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
