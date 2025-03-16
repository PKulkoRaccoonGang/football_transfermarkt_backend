from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet
from django.utils.html import mark_safe
from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Player model. Customizes how players are displayed
    and managed in the Django admin interface.
    """

    list_display = (
        "first_name",
        "last_name",
        "team",
        "market_value",
        "position",
        "jersey_number",
        "goals_scored",
        "assists_per_match",
        "shots_on_target",
        "pass_accuracy",
        "dribble_success",
        "shot_accuracy",
        "tackle_success",
        "yellow_cards",
        "red_cards",
        "get_photo_preview",
    )
    list_filter = ("team", "position", "country_code")
    search_fields = ("first_name", "last_name", "team__name", "country_code")
    readonly_fields = ("photo_preview", "team_photo_preview")
    actions = ["delete_photos"]

    def photo_preview(self, obj: Player) -> str:
        """
        Displays a large preview of the player's photo in the admin interface.
        """
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" style="max-height: 200px; max-width: 200px;" />'
            )
        return "No photo available"

    photo_preview.short_description = "Player Photo Preview"

    def team_photo_preview(self, obj: Player) -> str:
        """
        Displays a large preview of the player's team's photo in the admin interface.
        """
        if obj.team and obj.team.photo:
            return mark_safe(
                f'<img src="{obj.team.photo.url}" style="max-height: 200px; max-width: 200px;" />'
            )
        return "No team photo available"

    team_photo_preview.short_description = "Team Photo Preview"

    def get_photo_preview(self, obj: Player) -> str:
        """
        Displays a small preview of the player's photo in the admin list view.
        """
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" style="max-height: 50px; max-width: 50px;" />'
            )
        return "No photo"

    get_photo_preview.short_description = "Player Preview"

    def assists_per_match(self, obj: Player) -> float:
        """
        Calculates the average number of assists per match for the player.
        """
        if obj.matches_played > 0:
            return round(obj.assists / obj.matches_played, 2)
        return 0.0

    assists_per_match.short_description = "Assists per Match"

    def delete_photos(self, request: HttpRequest, queryset: QuerySet[Player]) -> None:
        """
        Deletes photos of selected players from storage.
        """
        count = 0
        for player in queryset:
            if player.photo:
                player.photo.delete()
                count += 1
        self.message_user(request, f"Photos for {count} players were deleted.")

    delete_photos.short_description = "Delete photos of selected players"

    ordering = ["last_name", "-goals_scored"]


admin.site.register(Player, PlayerAdmin)
