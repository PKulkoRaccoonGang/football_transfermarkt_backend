from django.db import models
from colorfield.fields import ColorField


class Team(models.Model):
    """
    Represents a football team with its details, including name, city, country,
    foundation year, stadium, coach, and team photo.
    """

    name = models.CharField(max_length=100, unique=True, verbose_name="Team Name")
    city = models.CharField(max_length=100, verbose_name="City")
    description = models.TextField(blank=True, verbose_name="Description")
    country = models.CharField(max_length=100, verbose_name="Country")
    foundation_year = models.PositiveIntegerField(verbose_name="Foundation Year")
    stadium = models.CharField(max_length=100, verbose_name="Stadium")
    coach = models.CharField(max_length=100, verbose_name="Coach")
    photo = models.ImageField(
        upload_to="team_photos/",
        blank=True,
        null=True,
        verbose_name="Team Photo",
    )
    primary_color = ColorField(
        default="#FFFFFF",
        verbose_name="Primary Color",
        help_text="Choose the team's primary color",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ["name"]
