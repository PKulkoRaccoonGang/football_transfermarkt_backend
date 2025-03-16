from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet
from django.utils.html import mark_safe
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Team model. Customizes how teams are displayed
    and managed in the Django admin interface.
    """

    list_display = (
        "name",
        "city",
        "country",
        "foundation_year",
        "stadium",
        "coach",
        "players_count",
        "get_photo_preview",
    )
    search_fields = ("name", "city", "country", "coach", "stadium")
    list_filter = ("country", "foundation_year")
    readonly_fields = ("photo_preview", "players_list")
    actions = ["delete_photos"]

    def photo_preview(self, obj: Team) -> str:
        """
        Displays a large preview of the team's photo in the admin interface.
        """
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" style="max-height: 200px; max-width: 200px;" />'
            )
        return "No photo available"

    photo_preview.short_description = "Photo Preview"

    def get_photo_preview(self, obj: Team) -> str:
        """
        Displays a small preview of the team's photo in the admin list view.
        """
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" style="max-height: 50px; max-width: 50px;" />'
            )
        return "No photo"

    get_photo_preview.short_description = "Preview"

    def players_count(self, obj: Team) -> int:
        """
        Counts the number of players associated with the team.
        """
        return obj.players.count()

    players_count.short_description = "Players Count"

    def players_list(self, obj: Team) -> str:
        """
        Generates an HTML list of players associated with the team, including photos.
        """
        players = obj.players.all()
        if not players.exists():
            return "No players in this team."

        player_list = []
        for player in players:
            player_photo = (
                f'<img src="{player.photo.url}" style="max-height: 50px; max-width: 50px; border-radius: 5px;" />'
                if player.photo
                else "No photo"
            )
            player_info = f"{player_photo} {player.first_name} {player.last_name} (#{player.jersey_number})"
            player_list.append(player_info)

        return mark_safe("<br>".join(player_list))

    players_list.short_description = "Players"

    def delete_photos(self, request: HttpRequest, queryset: QuerySet[Team]) -> None:
        """
        Deletes photos of selected teams from storage.
        """
        count = 0
        for team in queryset:
            if team.photo:
                team.photo.delete()
                count += 1
        self.message_user(request, f"Photos for {count} teams were deleted.")

    delete_photos.short_description = "Delete photos of selected teams"

    ordering = ["name"]


admin.site.register(Team, TeamAdmin)
