from django.contrib import admin
from .models import Event
from .models import Person
from .models import SailingClub
from .models import BoatType
from .models import Race
from .models import Entry


class EntryInline(admin.TabularInline):
    model = Event.entries.through
    fields = ('helm', 'crew', 'boat_type')
    extra = 0
    show_change_link = True


class RaceInline(admin.TabularInline):
    model = Race
    fields = ('number', 'start_time', 'end_time', 'sky_condition', 'wind_speed_min', 'wind_speed_max')
    extra = 0
    show_change_link = True


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('name', 'mode', 'start_date', 'end_date', 'race_count', 'race_unrated_on', 'organizer', 'race_committee', 'umpire')
    inlines = [
        EntryInline,
        RaceInline
    ]


class PlacementInline(admin.TabularInline):
    model = Race.placements.through
    fields = ('entry', 'finish_position', 'finish_time', 'status', 'calculated_time', 'calculated_place')
    readonly_fields = ('calculated_time', 'calculated_place')
    extra = 0


class RaceAdmin(admin.ModelAdmin):
    model = Race
    list_display = ('event', 'number', 'start_time', 'end_time', 'sky_condition', 'wind_speed_min', 'wind_speed_max')
    inlines = [
        PlacementInline,
    ]

admin.site.register(Event, EventAdmin)
admin.site.register(Person)
admin.site.register(SailingClub)
admin.site.register(BoatType)
admin.site.register(Race, RaceAdmin)
admin.site.register(Entry)
