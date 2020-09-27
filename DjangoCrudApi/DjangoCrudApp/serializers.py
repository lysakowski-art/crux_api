from rest_framework import serializers
from DjangoCrudApp.models import Routes
from DjangoCrudApp.models import Pages
from DjangoCrudApp.models import Regions


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routes
        fields = ('_id',
                  'route_title',
                  'route_author',
                  'route_rank',
                  'route_type',
                  'region',
                  'placemant_and_belay_anchor',
                  'route_description',
                  'location')


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pages
        fields = (
            '_id',
            'page_title',
            'page_content'
        )
class RegionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Regions
        fields = (
            '_id',
            'region_name',
            'group_of_regions'
        )
