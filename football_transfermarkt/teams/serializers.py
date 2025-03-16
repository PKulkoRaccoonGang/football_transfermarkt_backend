from rest_framework import serializers
from .models import Team
from players.serializers import PlayerSerializer


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the Team model.

    Includes all fields of the Team model and a nested list of players as a read-only field.

    Example response:
    {
        "id": 1,
        "name": "Inter Miami",
        "city": "Miami",
        "description": "A professional football club based in Miami.",
        "country": "USA",
        "foundation_year": 2018,
        "stadium": "DRV PNK Stadium",
        "coach": "Gerardo Martino",
        "photo": "http://example.com/media/team_photos/inter_miami.jpg",
        "primary_color": "#FF69B4",
        "players": [
            {
                "id": 1,
                "first_name": "Lionel",
                "last_name": "Messi",
                "position": "FW"
            },
            {
                "id": 2,
                "first_name": "Sergio",
                "last_name": "Busquets",
                "position": "MF"
            }
        ]
    }
    """

    players: PlayerSerializer = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model: type[Team] = Team
        fields: str = "__all__"
