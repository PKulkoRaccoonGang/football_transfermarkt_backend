from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Player model.

    Provides all fields of the Player model, with the team name as a read-only field.

    Example response:
    {
        "id": 1,
        "first_name": "Lionel",
        "last_name": "Messi",
        "birth_date": "1987-06-24",
        "country_code": "ARG",
        "team": "Inter Miami",
        "market_value": "50000000.00",
        "position": "FW",
        "jersey_number": 10,
        "goals_scored": 30,
        "assists": 20,
        "matches_played": 25,
        "shots_on_target": 50,
        "pass_accuracy": "85.5",
        "dribble_success": "88.0",
        "shot_accuracy": "75.0",
        "tackle_success": "60.0",
        "tackles": 10,
        "yellow_cards": 2,
        "red_cards": 0,
        "photo": "http://example.com/media/player_photos/messi.jpg"
    }
    """

    team: serializers.CharField = serializers.CharField(
        source="team.name", read_only=True
    )

    class Meta:
        model: type[Player] = Player
        fields: str = "__all__"
