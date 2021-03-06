from rest_framework import serializers
from .models import SailingClub
from .models import Person
from .models import Event
from .models import BoatType
from .models import Entry
from .models import Race
from .models import Placement


class SailingClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SailingClub
        fields = ('id', 'url', 'name', 'abbreviation', 'registration', 'was_organizer')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'url', 'first_name', 'last_name', 'sailing_club')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    entries = serializers.HyperlinkedRelatedField(source='entry_set', many=True, read_only=True, view_name='entry-detail')
    races = serializers.HyperlinkedRelatedField(source='race_set', many=True, read_only=True, view_name='race-detail')

    class Meta:
        model = Event
        fields = ('id', 'url', 'name', 'mode', 'start_date', 'end_date', 'race_count', 'race_unrated_on',
                  'organizer', 'race_committee', 'umpire', 'assistants', 'entries', 'races')


class BoatTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoatType
        fields = ('id', 'url', 'name', 'yardstick')


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'url', 'event', 'helm', 'crew', 'boat_type')


class PlacementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Placement
        fields = ('id', 'url', 'race', 'entry', 'finish_position', 'finish_time', 'status', 'calculated_time', 'calculated_place')
        read_only_fields = ('calculated_time', 'calculated_place')


class RaceSerializer(serializers.HyperlinkedModelSerializer):
    placements = serializers.HyperlinkedRelatedField(source='placement_set', many=True, read_only=True, view_name='placement-detail')

    class Meta:
        model = Race
        fields = ('id', 'url', 'event', 'number', 'start_time', 'end_time', 'sky_condition', 'wind_speed_min', 'wind_speed_max', 'placements')
